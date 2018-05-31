# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
class pageLinks(scrapy.Spider):
    name = "jobpagelinks"
    allowed_domains = ["jobkorea.co.kr"]
    start_urls = ['http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C%2C%2C%2C%2C%2C%2C%2C%2C10016%2C%2C%2C%2C%2C%2C%2C%2C%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=4']
    #start_urls = ['http://www.jobkorea.co.kr/starter/']
    company_page=[]
    def parse(self, response): #페이지의 기업 홈페이지 주소를 스크래핑함
        #1.모든 페이지 다 돌면서 제목 링크 따오기..
        #2.urljoin으로 www.jobkorea.co.kr/Recruit 어쩌고

        '''next_page = response.css('div.info > div.tit > a.link::attr(href)')[0].extract()  # 제목 클릭 후 상세 페이지
        if next_page:
            next_page = response.urljoin(next_page)
            # self.log('I just visited: ' + next_page.url)
            yield scrapy.Request(url=next_page, callback=self.parse)'''
        self.log('I just visited: ' + response.url)
        #기업 상세 페이지. 여기서 홈페이지 등
        for cp in response.css('li > div.info > div.tit > a::attr(href)').extract():
            self.company_page.append('http://www.jobkorea.co.kr'+cp)
        #기업 홈페이지
        for link in response.css('a.devCoHomepageLink::attr(href)').extract():
            self.log('2')
            item = {
                'homepage':link
            }
            self.log('5')
            yield item
        #다음 페이지로 이동하기 1,2,3...
        next_page = response.css('div.tplPagination > ul > li > a::attr(href)')[0].extract()
        if next_page:
            next_page = response.urljoin(next_page)
            self.log('Page: ' + next_page.url)
            yield scrapy.Request(url=next_page, callback=self.parse)
