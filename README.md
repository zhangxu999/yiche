# yiche
一个爬取易车网汽车数据的爬虫，使用 python scrapy框架。
使用scrapy-redis 作为分布式工具。


##依赖
  * python2(2.7或以上)
  * scrapy 1.2.0
  * scrapy-redis 0.6.3

##输入输出
  汽车数据爬取初始url: http://api.car.bitauto.com/CarInfo/getlefttreejson.ashx?tagtype=chexing
  数据输出:chexing.json(各大汽车品牌基本数据）,data_cars.csv(详细汽车款型数据)
 
##运行
#####进入项目根目录下，运行命令:
```python
scrapy crawl yiche
```
