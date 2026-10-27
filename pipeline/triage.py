#Date: 2026-10-26
#Purpose: Free, rule-based triage of fetched papers before any language model sees them. High recall by design:
#  route A = abstract says it introduces something and mentions sequencing/profiling;
#  route B = full text (open access only) contains a naming phrase ("an approach we call X", "creating X, which ...")
#  near assay words - this is what catches methods buried in Results (TOPmentation, Paired Hi-C).
#Usage: python pipeline/triage.py data/raw_2026-10-12.jsonl > data/candidates_2026-10-12.jsonl
#  Or import: triage(record, fetch_fulltext=True) -> {"flag": bool, "routes": [...], "names": [...]}
#INPUT: JSONL records from fetch.py

import json
import re
import sys

from fetch import full_text

INTRODUCES = re.compile(r"\b(?:here,? )?we (?:present|develop(?:ed)?|introduce|report|describe|establish(?:ed)?|devise[d]?|"
                        r"engineer(?:ed)?|optimi[sz]ed|adapted|refined|modified|extended)\b", re.I)
ASSAY_WORDS = re.compile(r"sequencing|-seq\b|\bseq\b|profiling|single[- ]cell|spatial(?:ly)?|\bassay|\bprotocol|"
                         r"chromatin|transcriptom|epigenom|methylom|library prep|tagmentation|barcod", re.I)
# A method-like name: first token may start lowercase (tRNAZAP, scHi-C); later tokens are Capitalised or hyphenated
# (Droplet Hi-C, Transcription factor-OPtimized ChIPmentation). Max 4 tokens. Verbs are case-insensitive via (?i:...).
TOK1, TOKN = r"[A-Za-z0-9][\w&+/-]*", r"(?:[A-Z0-9][\w&+/-]*|[a-z]+-[\w&+/-]+)"
NAME = rf"({TOK1}(?: {TOKN}){{0,3}})"
NAMING = [re.compile(p) for p in (
    rf"\b(?i:(?:that |which )?we (?:call|term|name|dub)(?:ed)?) [\"“']?{NAME}",
    rf"\b(?i:termed|dubbed|hereafter|referred to as|named) [\"“'(]?{NAME}",
    rf"\b(?i:creating|yielding|resulting in|establishing|developing) [\"“']?{NAME}[\"”']?, (?i:which|a|an|that)\b",
    rf"\b(?i:we (?:present|introduce|developed|develop|report|describe|establish(?:ed)?)) [\"“']?{NAME}[\"”']?[,:(]",
)]
ACRONYM = re.compile(r"^\s*\(\s*([A-Za-z0-9][\w&+/-]{1,24})\s*[,;)]")  # "Long Name (ACRO, ..." -> ACRO
STOP_NAMES = {"We", "Here", "This", "These", "The", "Our", "It", "In", "Fig", "Figure", "Supplementary", "Extended", "Data", "Methods"}


def plausible(name):
    """Method names have an internal capital, a digit, or a hyphen (Hi-C, tRNAZAP, 2C-RT); plain words don't."""
    return (name.split()[0] not in STOP_NAMES and 2 <= len(name) <= 60
            and bool(re.search(r"(?<=.)[A-Z]|\d|-|&", name)))


def names_in(text, window=300):
    """Method-like names introduced by a naming phrase with assay words nearby."""
    found = []
    for pat in NAMING:
        for m in pat.finditer(text):
            if not ASSAY_WORDS.search(text[max(0, m.start() - window): m.end() + window]):
                continue
            cands = m.group(1).strip(" .,;:)\"”'").split("/")
            acro = ACRONYM.match(text[m.end(): m.end() + 40])
            cands += [acro.group(1)] if acro else []
            found += [c for c in cands if plausible(c) and c not in found]
    return found


def triage(rec, fetch_fulltext=True):
    head = f"{rec.get('title', '')}. {rec.get('abstract', '')}"
    # submissions and watchlist rows (human-picked) are never discarded here
    routes = (["submitted"] if rec.get("submitted") else []) + (["watchlist"] if rec.get("watchlist") else [])
    names = names_in(head)
    for given in (rec.get("submitted_name"), rec.get("watchlist_name")):
        if given and given not in names:
            names.insert(0, given)
    if INTRODUCES.search(head) and ASSAY_WORDS.search(head):
        routes.append("abstract")
    if fetch_fulltext:
        body = full_text(rec)
        if body:
            extra = [n for n in names_in(body) if n not in names]
            if extra:
                routes.append("fulltext-naming")
                names += extra
    return {"flag": bool(routes), "routes": routes, "names": names}


if __name__ == "__main__":
    n = kept = 0
    for line in open(sys.argv[1]):
        rec = json.loads(line)
        n += 1
        t = triage(rec)
        if t["flag"]:
            kept += 1
            print(json.dumps(rec | {"triage": t}))
    print(f"{kept}/{n} records kept by triage", file=sys.stderr)
