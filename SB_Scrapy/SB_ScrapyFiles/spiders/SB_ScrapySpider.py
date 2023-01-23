# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy

class PubMedSpider(scrapy.Spider):
    name = "pubmed"
    start_urls = ["https://pubmed.ncbi.nlm.nih.gov/"]
    
    def parse(self, response):
        # Extract the links to the publications
        links = response.xpath("//a[@class='labs-docsum-title']/@href").getall()
        for link in links:
            yield response.follow(link, self.parse_publication)
        
        # Follow the next page link
        next_page = response.xpath("//a[@class='next']/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)

#### Xpath selectors need to be modified for the structure of the website
            
    def parse_publication(self, response):
        # Extract the information from the publication page
        title = response.xpath("//h1[@class='article-title']/text()").get()
        authors = response.xpath("//span[@class='authors']/text()").get()
        abstract = response.xpath("//p[@class='abstract']/text()").get()
        yield {'title': title, 'authors': authors, 'abstract': abstract}
