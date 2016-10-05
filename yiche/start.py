import  scrapy
from spiders.YicheSpider import YicheSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(YicheSpider)

process.start()