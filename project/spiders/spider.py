# coding! utf-8
import scrapy
from scrapy.linkextractors import LinkExtractor
#from scrapy.spiders import CrawlSpider, Rule
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from project.items import YYItem
import re


class yy_Spider(scrapy.Spider):
    # 爬虫名
    name = 'YY'
    # 允许的域名
    allowed_domains = ['www.cfcpn.com', 'www.ccgp.gov.cn']
    offset = 0
    base_url = 'http://www.ccgp.gov.cn/cggg/zygg/'
    # 爬虫的起始url
    start_urls = [base_url + 'index.htm']

    def parse(self, response):
        item = YYItem()
        items = response.xpath('//div[@class="vF_detail_relcontent_lst"]/ul/li')
        for each in items:
            item['name'] = each.xpath('.//a/text()').extract()[0]
            item['time'] = each.xpath('.//em[2]/text()').extract()[0]
            # '2020-02-11 16:08'
            item['unit'] = each.xpath('.//em[last()]/text()').extract()[0]
            item['address'] = self.base_url + each.xpath('.//a/@href').extract()[0].replace('./', '')
            item['sources'] = u'中国政府采购网中央公告'
            # 将数据发送给管道
            yield item
        if self.offset < 1:
            self.offset += 1
        # 将请求重新发送给调度器
        yield scrapy.Request(self.base_url + 'index_' + str(self.offset) + '.htm', callback=self.parse)

