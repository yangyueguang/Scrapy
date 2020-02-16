# -*- coding: utf-8 -*-

BOT_NAME = 'project'  # 爬虫名称
SPIDER_MODULES = ['project.spiders']  # 爬虫应用路径
NEWSPIDER_MODULE = 'project.spiders'
# 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
DEPTH_LIMIT = 4
# 遵守robots.txt规则
ROBOTSTXT_OBEY = False
# 允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True
LOG_ENABLED = True
LOG_STDOUT = False
LOG_FILE = "root.log"
LOG_LEVEL = "DEBUG"

# 最大并发量
CONCURRENT_REQUESTS = 16
# 单域名访问并发数，并且延迟下次秒数也应用在每个域名，比CONCURRENT_REQUESTS更加细致的并发
CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 单IP访问并发数，如果有值则忽略：CONCURRENT_REQUESTS_PER_DOMAIN，
CONCURRENT_REQUESTS_PER_IP = 16
# 访问相同的网页延迟时间
DOWNLOAD_DELAY = 3
# 是否启用cookie
COOKIES_ENABLED = False
# 是否是调试模式，调试模式下每次得到cookie都会打印
COOKIES_DEBUG = True
# Telnet用于查看当前爬虫的信息(爬了多少，还剩多少等)，操作爬虫(暂停等)等...， cmd中:telnet 127.0.0.1 6023(6023是专门给爬虫用的端口)
TELNETCONSOLE_ENABLED = True
# 0或1。0深度优先，一下找到底，然后再找其他的 1广度优先，一层一层找他们内部的原理就是根据response.meta里的depth(层数)来找。
DEPTH_PRIORITY = 0
# 使用了scrapy-redis里的去重组件，不使用scrapy默认的去重
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用了scrapy-redis里的调度器组件，不实用scrapy默认的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用队列形式
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 管道文件
ITEM_PIPELINES = {
    'project.pipelines.YYPipeline': 300,
}
# 爬虫中间件
SPIDER_MIDDLEWARES = {
    'project.middlewares.CustomSpiderMiddleware': 100,
}
# 下载中间件
DOWNLOADER_MIDDLEWARES = {
    'project.middlewares.RandomUserAgentDownloadMiddleware': 100,
    # 'project.middlewares.SeleniumDownloadMiddleware': 200
}
# 是否启用扩展
EXTENSIONS = {
   'project.middlewares.MyExtend': 100,
}
# 客户端 user-agent请求头，常伪造成浏览器
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    # 'Cookie': 'SESSIONID=3d6579cc39d5b0a100aa83b604d696a0968f0c55; SESSIONID=3d6579cc39d5b0a100aa83b604d696a0968f0c55; UM_distinctid=17037d4b468653-0a70bdbf91f194-39647b0e-1aeaa0-17037d4b4698b0; CNZZDATA1261815924=413849371-1581480415-%7C1581480415; Hm_lvt_72331746d85dcac3dac65202d103e5d9=1581484652; Hm_lpvt_72331746d85dcac3dac65202d103e5d9=1581485162; userid_secure=fqa6+CEcAQuGQP2cO6B+cVzzRjpA7JmR8uIlfhIfU3AgDjX7qOaUu0O0eeYpQ9jtGFDlMZJLxMfpKX2IFJrpgAqQM2U/GdH+iFkNw8vCPozCEOAPfrFPgZ+MHi6/FOpodbWZan3+pz0g/W6NGRLRFSbabFS5cMVkIOsBpUBuQ8AdFiBXZAuJdbNxPeAnP+NpeHNMki+9MRfUp6D3l6kGPUKWBFozx40H1GgAycTLzCuoRGSPRq5E+ct0KIoOZgEmPOROpXo2ja5Wt2N+fvUYdQoxxpkFcbcj51pSBw43d6hVAlvc2D5h9zU9OKgQMFPE2BS02EWxjBtzweIT9pcmmyoqKjIwMjAtMDItMDkgMDA6MDA6MDA=',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
}
# 自动限速算法(智能请求)
AUTOTHROTTLE_ENABLED = True
# 第一次下载延迟几秒
AUTOTHROTTLE_START_DELAY = 5
# 最大延迟
AUTOTHROTTLE_MAX_DELAY = 60
# 波动范围，不用管
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示收到的每个响应的限制状态
AUTOTHROTTLE_DEBUG = True

# 是否开启网页缓存
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

