# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# mogodb数据库
# from pymongo import MogoClient
# client = MogoClient()
# collection = client["tencent"]["hr"]
#导入items
from tencent.items import TencentItem
class TencentPipeline(object):
    def process_item(self, item, spider):
        # print(spider.name)
        if isinstance(item,TencentItem):


            print(item)
        # collection.insert(dict(item))
        return item

