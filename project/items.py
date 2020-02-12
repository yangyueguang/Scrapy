# coding! utf-8
import scrapy


class YYItem(scrapy.Item):
    name = scrapy.Field()  # 项目名称
    unit = scrapy.Field()  # 采购单位
    time = scrapy.Field()  # 发布时间
    address = scrapy.Field()  # 原文地址
    sources = scrapy.Field()  # 数据来源
