# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 可以定义多个item对应不同的爬虫项目字段，比如怕京东，抽屉，汽车之家
#然后再pipelines中做判断
class TencentItem(scrapy.Item): #scrapy.Item也是一个字典
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    title = scrapy.Field()   #scrapy.Field()是一个字典
    position = scrapy.Field()
    publish_date = scrapy.Field()


class ChoutiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    position = scrapy.Field()
    publish_date = scrapy.Field()


class JdItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    position = scrapy.Field()
    publish_date = scrapy.Field()