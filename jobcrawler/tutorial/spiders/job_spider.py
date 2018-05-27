# -*- coding: utf-8 -*-
import scrapy

from tutorial.items import TutorialItem

class JobSpider(scrapy.Spider):
    name = "jobspider"
    allowed_domains = ["jobkorea.co.kr"]
    start_urls=[
        "http://www.jobkorea.co.kr/starter/?schLocal=&schPart=10016&schMajor=&schEduLevel=&schWork=&schCType=&isSaved=1&LinkGubun=0&LinkNo=0&Page=1&schType=0&schGid=0&schOrderBy=0&schTxt="
        #"http://www.jobkorea.co.kr"
    ]
    def parse(self, response):
        infos = response.xpath('//*[@id="devStarterForm"]/div[2]/ul//li')
        for info in infos:
            item = TutorialItem()
            item['company'] = info.xpath('div[1]/div[1]/a/text()')[0].extract()
            item['title'] = info.xpath('div[2]/div[1]/a/span/text()')[0].extract()
            item['job'] = info.xpath('div[2]/div[2]//span/text()')[0].extract()
            #item['deadline'] = info.xpath('div[4]/span[3]/text()')[0].extract()
            item['deadline'] = info.xpath('div[4]//span/text()')[0].extract()
            yield item
    #파일로 만들기
    '''def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)'''
    '''def parse(self, response):
        print('*****직업*****')
        #response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[1]/div[1]/a/@href').extract()
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[1]/div[1]/a/text()')[0].extract()) company
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[2]/div[1]/a/span/text()')[0].extract()) title
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[2]/div[2]//span/text()')[0].extract()) job
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[3]/strong/text()')[0].extract()) career
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[3]//span/text()')[0].extract()) 학력
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[3]//span/text()')[1].extract()) location
        #print(response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]/div[4]/span[3]/text()')[0].extract()) deadline
        for info in response.xpath('//*[@id="devStarterForm"]/div[2]/ul/li[1]'):
            company = info.xpath('div[1]/div[1]/a/text()')[0].extract()
            title = info.xpath('div[2]/div[1]/a/span/text()')[0].extract()
            job = info.xpath('div[2]/div[2]//span/text()')[0].extract()
            deadline = info.xpath('div[4]/span[3]/text()')[0].extract()
            #print(company,title,job,deadline)
            print(company)
            print(title)
            print(job)
            print(deadline)'''


