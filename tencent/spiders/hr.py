# -*- coding: utf-8 -*-
import scrapy

#导入items
from tencent.items import TencentItem

class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        print("=========")
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1] #去掉第一个和最后一个

        for tr in tr_list:
            # 使用item，items里面的字段要和这下面的字段一样
            item = TencentItem()
            # item = {}  #不使用items

            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["position"] = tr.xpath("./td[4]/text()").extract_first()
            item["publish_date"] = tr.xpath("./td[5]/text()").extract_first()
            yield item

            # <a href="javascript:;"class="noactive" id="next">下一页</a>
            #判断下一页，最后一页的href="javascript
        next_url = response.xpath("//a[@id='next']/@href").extract_first()
        if next_url != "javascript": #如果href的属性不为javascript，代表有下一页
            next_url = 'https://hr.tencent.com/'+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )



