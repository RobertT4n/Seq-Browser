#Date: 2026-10-28
#Purpose: Decide whether a phrase is really the expansion of a method's acronym, and pull the authors' own expansion out
#  of a paper's text. Shared by the full_name backfill and pipeline/test_guards.py so the rule is defined in exactly one
#  place. Deliberately strict: a wrong expansion is worse than none (mtscATAC-seq was once given plain ATAC-seq's).
#Usage: from acronym import matches, expansion
#INPUT: none (pure functions).

import re

STOP = re.compile(r"^(?:we (?:call|term|name|present|report|developed?|introduce)\s+(?:it\s+)?|termed\s+|named\s+|"
                  r"called\s+|a new method\s+|the\s+)", re.I)


def words(s):
    """Word tokens, splitting hyphens too: 'contiguity-preserving' -> ['contiguity', 'preserving']."""
    return re.findall(r"[A-Za-z0-9]+", s)


def initials(s):
    return "".join(w[0].upper() for w in words(s))


def core(name):
    """The name without a trailing '-seq'/'sequencing', which expansions spell out as a word rather than a letter."""
    return re.sub(r"(?i)[-\s]?(seq|sequencing)$", "", name)


def acronym_letters(name):
    """The letters an expansion must supply, in order. A CAPITAL contributes itself; a lowercase run of >=4 characters is
    a spelled-out word and contributes its first letter ('microSPLiT' -> 'MSPLT', because the M is 'Microbial').
    Short lowercase runs ('sc', 'sn', 'mt'... <4) are conventional prefixes that expansions usually leave implicit, so
    they contribute nothing: 'scCAT-seq' -> 'CAT'."""
    out = []
    for m in re.finditer(r"[A-Z0-9]|[a-z]+", core(name)):
        tok = m.group(0)
        if tok.islower():
            if len(tok) >= 4:
                out.append(tok[0].upper())
        else:
            out.append(tok)
    return "".join(out)


def lowercase_parts(name):
    """Lowercase chunks of the name that are words in their own right, not acronym letters:
    'HT-recruit' -> ['recruit']; 'mtscATAC-seq' -> ['mtsc']; 'microSPLiT' -> ['micro']. Short ones (<4) are ignored
    because they are conventional prefixes ('sc', 'sn') that expansions often leave implicit."""
    out = []
    for seg in re.split(r"[-\s_]+", core(name)):
        for chunk in re.findall(r"[a-z]+", seg):
            if len(chunk) >= 4:
                out.append(chunk)
    return out


def matches(name, phrase):
    """True only if `phrase` plausibly expands `name`:
    1. every CAPITAL letter of the name appears among the phrase's word initials, and the first initial matches;
    2. every lowercase word-chunk of the name (>=4 chars) is actually accounted for in the phrase.
    Rule 2 is what stops 'Assay for Transposase Accessible Chromatin with sequencing' from being read as the expansion
    of mtscATAC-seq, and 'High-throughput method' as that of HT-recruit."""
    want, ini = acronym_letters(name), initials(phrase)
    if not want or not ini or ini[0] != want[0] or not all(c in ini for c in want):
        return False
    low = phrase.lower()
    return all(chunk[:4] in low for chunk in lowercase_parts(name))


def expansion(name, text):
    """The authors' own expansion of `name` in `text`, as '<words> (NAME)' or 'NAME (<words>)', or None.
    Lead-in words ('we developed a protocol to capture Chromatin Accessibility...') are trimmed; of the candidates that
    pass `matches`, the tightest is returned."""
    esc = re.escape(name).replace(r"\-", "[-‐ ]?").replace(r"\ ", "[ -]?")
    want = acronym_letters(name)
    if len(want) < 2:
        return None
    best = None
    for pat in (rf"([^.;:()]{{6,200}}?)\s*\(\s*{esc}\s*[,;)]", rf"{esc}\s*\(([^)]{{6,200}}?)\)"):
        for m in re.finditer(pat, text, re.I):
            cand = STOP.sub("", re.sub(r"\s+", " ", m.group(1)).strip(" ,;:-—")).strip()
            ws = cand.split()
            for i in range(len(ws)):                       # drop lead-in words; keep the tightest phrase that still fits
                sub = " ".join(ws[i:])
                if len(ws) - i >= 2 and len(initials(sub)) <= len(want) + 4 and matches(name, sub):
                    if best is None or len(initials(sub)) < len(initials(best)):
                        best = sub[0].upper() + sub[1:]
    return best

# ---- Provenance ----
# Upstream:   none (pure text rules)
# Downstream: pipeline/test_guards.py (synthetic cases), the full_name backfill, pipeline/CLASSIFIER_INSTRUCTIONS.md
# References: the real mislabels that motivated each rule - ChAIR, HiCAR, CPT-seq, microSPLiT (accept);
#             mtscATAC-seq given ATAC-seq's expansion, HT-recruit given "High-throughput method" (reject)
# Notes:      precision over recall by design: most abstracts never spell the acronym out, so a miss is expected and a
#             wrong expansion is not. full_name is required in the classifier template, so new entries get it from the paper.
