# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import TutorialItem
from scrapy import Request
class pageLinks(scrapy.Spider):
    name = "test"
    allowed_domains = ["jobkorea.co.kr"]
    #start_urls = ['http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C%2C%2C%2C%2C%2C%2C%2C%2C10016%2C%2C%2C%2C%2C%2C%2C%2C%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=4']
    #start_urls = ['http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=']
    start_urls = ['http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt=']

    def parse(self, response): #페이지의 기업 홈페이지 주소를 스크래핑함
        self.log('I just visited: ' + response.url)
        infos = response.xpath('//*[@id="devStarterForm"]/div[2]/ul//li')
        for info in infos:
            item = TutorialItem()
            item['company_name'] = info.xpath('div[1]/div[1]/a/text()')[0].extract()
            link = info.xpath('div[1]/div[1]/a/@href')[0].extract()
            if link[0] == '/':
                self.log('first char is /')
                item['company_info'] = 'www.jobkorea.co.kr'+info.xpath('div[1]/div[1]/a/@href')[0].extract()
            elif link[0] == 'h':
                item['company_info'] = info.xpath('div[1]/div[1]/a/@href')[0].extract()
            item['title'] = info.xpath('div[2]/div[1]/a/span/text()')[0].extract()
            deadline = info.xpath('div[4]/span[@class="day"]/text() | div[4]/span[@class="day schedule"]/text() | div[4]/span[@class="day tomorrow"]/text()')[:].extract()
            item['deadline'] = deadline
            item['achievement'] = info.xpath('div[3]/span[1]/text()')[0].extract()
            item['career'] = info.xpath('div[3]/strong/text()')[0].extract()
            item['area'] = info.xpath('div[3]/span[2]/text()')[0].extract()
            item['job'] = info.xpath('div[2]/div[2]/span/text()')[:].extract()
            yield item
            #item['job'] = info.xpath('div[2]/div[2]/span/text()')[0].extract()
        '''div = response.xpath('//*[@id="devStarterForm"]/div[2]/ul//li')
        for i in div:
            x = i.xpath('div[2]/div[2]/span/text()')[:].extract()
            item['job'] = x[:]
            yield item'''

'''next_page = response.css('div.tplPagination > ul > li > a::attr(href)')[0].extract()
        if next_page:
            next_page = response.urljoin(next_page)
            self.log('Page: ' + next_page.url)
            yield scrapy.Request(url=next_page, callback=self.parse)
'''