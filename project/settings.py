# -*- coding: utf-8 -*-

BOT_NAME = 'project'
SPIDER_MODULES = ['project.spiders']
NEWSPIDER_MODULE = 'project.spiders'


USER_AGENTS = [
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2)',
    'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
    'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
    'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; zh-cn; M032 Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Windows; U; Windows NT 5.2) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13'
]
#
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'SESSIONID=3d6579cc39d5b0a100aa83b604d696a0968f0c55; SESSIONID=3d6579cc39d5b0a100aa83b604d696a0968f0c55; UM_distinctid=17037d4b468653-0a70bdbf91f194-39647b0e-1aeaa0-17037d4b4698b0; CNZZDATA1261815924=413849371-1581480415-%7C1581480415; Hm_lvt_72331746d85dcac3dac65202d103e5d9=1581484652; Hm_lpvt_72331746d85dcac3dac65202d103e5d9=1581485162; userid_secure=fqa6+CEcAQuGQP2cO6B+cVzzRjpA7JmR8uIlfhIfU3AgDjX7qOaUu0O0eeYpQ9jtGFDlMZJLxMfpKX2IFJrpgAqQM2U/GdH+iFkNw8vCPozCEOAPfrFPgZ+MHi6/FOpodbWZan3+pz0g/W6NGRLRFSbabFS5cMVkIOsBpUBuQ8AdFiBXZAuJdbNxPeAnP+NpeHNMki+9MRfUp6D3l6kGPUKWBFozx40H1GgAycTLzCuoRGSPRq5E+ct0KIoOZgEmPOROpXo2ja5Wt2N+fvUYdQoxxpkFcbcj51pSBw43d6hVAlvc2D5h9zU9OKgQMFPE2BS02EWxjBtzweIT9pcmmyoqKjIwMjAtMDItMDkgMDA6MDA6MDA=',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
# 遵守robots.txt规则
# ROBOTSTXT_OBEY = True
# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 使用队列形式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True
# 配置管道文件
ITEM_PIPELINES = {
    'project.pipelines.YYPipeline': 300,
    # 'scrapy_redis.pipelines.RedisPipeline' : 400,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'youyuan (+http://www.yourdomain.com)'


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False



# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'youyuan.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'youyuan.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}



# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 以下是自定义配置信息
EXCEL_FILE = '/Users/supers/Desktop/result.xlsx'
WORDS = ['rpa', 'RPA', '流程自动化', '流程机器人', '业务自动化', '推荐', '智能', '技术支撑', 'NLP', '自然语言处理']
WORDS2 = ['数据中台', '知识图谱', '自然语言理解', '文档智能检索', 'NLP']
FROM_EMAIL = '222@qq.com'
FROM_PWD = '123456'
TO_EMAIL = '2323@qq.com'
SMTP_SERVER = 'smtp.qq.com'

