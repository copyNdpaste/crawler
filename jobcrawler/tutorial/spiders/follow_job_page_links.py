# -*- coding: utf-8 -*-
'''import scrapy
from scrapy import Request
class pageLinks(scrapy.Spider):
    name = "jobpagelinks"
    allowed_domains = ["jobkorea.co.kr"]
    start_urls = ['http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C10016%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=1']
    company_page=[] #사이트의 1, 2, 3, ... n 번째 페이지까지 다 돌면서 제목에 있는 url로 진입, 각각의 url에서 필요한 item 따오기.

    def parse(self, response): #페이지의 기업 홈페이지 주소를 스크래핑함
        #1.모든 페이지 다 돌면서 제목 링크 따오기..
        #2.urljoin으로 www.jobkorea.co.kr/Recruit 어쩌고
        #제목 링크
        #response.xpath('//*[@id="devStarterForm"]/div[2]/ul//li/div[2]/div[1]/a/@href').extract()
        #다음 페이지 이동
        #response.xpath('//*[@id="devStarterForm"]/div[2]/div/ul/li[2]/a/@href')[0].extract()
            yield item
'''