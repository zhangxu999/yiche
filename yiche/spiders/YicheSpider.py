#coding:utf-8
import scrapy
from util import fixjson, json2csv_chexing,json2csv_chexing3
import logging
import  json
class YicheSpider(scrapy.Spider):
    name = "yiche"
    domain = "http://car.bitauto.com/"
    start_urls = ['http://api.car.bitauto.com/CarInfo/getlefttreejson.ashx?tagtype=chexing']

    def parse(self,response):
        print '--------', response.body[:30], '------------'
        logging.log(logging.INFO,response.body[:20])
        filename = "chexing.csv"
        chexing = fixjson(response.body[14:-1])
        chexing_json = json.loads(chexing)
        with open(filename,'wb') as f:
            f.write(json2csv_chexing(chexing))
        self.log('Save file %s'%filename)
        mainBrand = chexing_json['brand']
        

        for letter in mainBrand:
            for car in mainBrand[letter]:
                url = car['url']
                request = scrapy.Request(url=(self.domain+url), callback=self.parse_chexing2)
                logging.log(logging.DEBUG, (self.domain+url))
                request.meta['mb'] = car['name']
                request.meta['store'] = f
                yield  request

    def parse_chexing2(self, response):

        xpath = '//div[@id="divCsLevel_0"]//div[@class="carpic_list"]//li/a[1]/@href'
        urls = map(lambda x: self.domain+x+'peizhi/', response.xpath(xpath).extract())
        f = open(response.meta['mb']+'.csv','w')
        for url in urls:
            request = scrapy.Request(url=url,callback=self.parse_chexing3)
            request.meta['store']=f
            yield request
        #f.close()


    def parse_chexing3(self, response):

        data = response.xpath('//script/text()')[6].extract()[27:-5]
        data_json = json.loads(data)
        f = response.meta['store']
        car_name = data_json[0][0][5]
        f.write(json2csv_chexing3(data))
        f.flush()
        self.log('Save car %s' % car_name)

















