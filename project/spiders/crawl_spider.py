# -*- coding: utf-8 -*-
import scrapy
import random
from project import conf
from project.items import YYItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']
    # 规则意味着html里面所有的链接符合规则的会继续往里面爬取 callback是用来响应子爬取的网页解析
    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), follow=True, process_links='deal_links', process_request='deal_request'),
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_detail'),
    )

    # 处理链接
    def deal_links(self, links):
        for link in links:
            print(link.url)
            link.url = link.url.replace('?', '&').replace('Type&', 'Type?')
        return links

    def deal_request(self, request, response):
        print(request.url)
        request.headers['User-Agent'] = random.choice(conf.user_agent_list)
        return request

    def parse_detail(self, response):
        item = YYItem()
        item['name'] = response.xpath('//span[@class="niae2_top"]/text()').extract()[0]
        item['unit'] = '采购单位'
        item['time'] = '2020-01-01 00:00'
        item['sources'] = self.name
        item['address'] = response.url
        yield item
