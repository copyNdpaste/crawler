# -*- coding: utf-8 -*-
import scrapy

class pageLinks(scrapy.Spider):
    name = "pagelinks"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response): #페이지의 저자명, 글자, 태그를 스크래핑함
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name':quote.css('small.author::text').extract_first(),
                'text':quote.css('span.text::text').extract_first(),
            }
            yield item
        #follow pagination link
        next_page = response.css("li.next>a::attr(href)")[0].extract()
        if next_page:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
