# coding: utf-8
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy_redis.spiders import RedisSpider
from project.items import YYItem
'''
# 启动redis
# 如果做分布式要解注释以下几个。redis_host redis_port 去重规则 调度规则 对列形式 管道文件要有scrapy_redis
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
ITEM_PIPELINES = {
    'project.pipelines.YYPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 使用
先连接同一个redis服务器
1. 各个地址启动爬虫
scrapy runspider $spider_py_path
2. 在redis客户端发送一条消息
> lpush $redis_key $start_url
'''

class MySpider(RedisSpider):
    name = 'YY'
    #allowed_domains = ['youyuan.com']
    #start_urls = ['http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/']
    redis_key = "yyspider:start_urls"

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(YySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        print(response.text)
        item = YYItem()
        item['name'] = ''
        item['unit'] = ''
        item['time'] = '2020-01-01 00:00'
        item['address'] = ''
        item['sources'] = self.name
        yield item


class YySpider(RedisCrawlSpider):
    name = 'YY'
    #allowed_domains = ['youyuan.com']
    #start_urls = ['http://www.youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p1/']
    redis_key = "yyspider:start_urls"
    rules = (
        Rule(LinkExtractor(allow=(r"youyuan.com/find/beijing/mm18-25/advance-0-0-0-0-0-0-0/p\d+/"))),
        Rule(LinkExtractor(allow=(r"youyuan.com/\d+-profile/")), callback="parse_item"),
    )

    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(YySpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        print(response.text)
        item = YYItem()
        item['name'] = ''
        item['unit'] = ''
        item['time'] = '2020-01-01 00:00'
        item['address'] = ''
        item['sources'] = self.name
        yield item
