# -*- coding: utf-8 -*-
'''
import scrapy
from tutorial.items import TutorialItem

class JobHomeSpider(scrapy.Spider):
    name = "jobhomespider"
    allowed_domains=["jobkorea.co.kr"]
    start_url = ["http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schPart=%2C%2C%2C%2C%2C%2C%2C%2C%2C10016%2C%2C%2C%2C%2C%2C%2C%2C%2C&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=4"]
    #start_url=["http://www.jobkorea.co.kr/"]
    base_url='http://www.jobkorea.co.kr'
    def parse(self, response):
        #제목의 href
        for href in response.xpath('//*[@id="devStarterForm"]/div[2]/ul//li/div[2]/div[1]/a/@href')[0].extract():
            #url = response.urljoin('http://www.jobkorea.co.kr',href)#제목의 링크..
            self.log("hi")
            url = self.base_url+ href # 제목의 링크..
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    def parse_dir_contents(self,response):
        for home in response.xpath('//*[@class="logo"]/a/@href')[0].extract():
            item=TutorialItem()
            #item['homepage'] = JobHomeSpider.start_url[0]+home[0].extract()
            item['homepage'] = self.base_url+home
            print(item)
            yield item
'''