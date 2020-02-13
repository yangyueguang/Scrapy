# coding! utf-8
import base64
import time
import random
import scrapy
import requests
from project import conf
from selenium import webdriver
from selenium.common.exceptions import TimeoutException


# 下载中间件
class RandomUserAgentDownloadMiddleware(object):
    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(conf.user_agent_list)
        request.meta["proxy"] = "http://" + random.choice(conf.ip_pool)
        # 私有代理池
        # proxy = random.choice(conf.private_ip_pool)
        # proxy_user_pass = proxy['username'] + ':' + proxy['password']
        # encoded_user_pass = base64.b64encode(proxy_user_pass.encode('utf-8'))
        # request.meta['proxy'] = "http://" + proxy['ip']
        # request.headers['Proxy-Authorization'] = 'Basic ' + str(encoded_user_pass, encoding="utf-8")

    def process_response(self, request, response, spider):
        if response.status != 200:
            request.meta['proxy'] = "http://" + random.choice(conf.ip_pool)
            return request
        return response


class LiantongDownloadMiddleware(object):
    def __init__(self):
        self.se = requests.session()

    def process_request(self, request, spider):
        home_url = request.meta.get('url')
        if request.meta.get('isHome'):
            self.se.get(home_url)
        res = self.se.post(request.url)
        return scrapy.http.HtmlResponse(url=request.url, body=res.text, request=request, encoding='utf-8', status=200)


class SeleniumDownloadMiddleware(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=60)

    def __init__(self, timeout=5):
        self.timeout = timeout
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chromedriver_path = '/usr/local/bin/chromedriver'
        self.browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
        self.browser.set_window_size(2000, 5000)
        self.browser.set_page_load_timeout(10)
        self.wait = webdriver.support.ui.WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        page = request.meta.get('page', 1)
        try:
            if page == 1:
                self.browser.get(request.url)
            elif 1 < page < 5:
                next_element = self.browser.find_element_by_xpath('//*[@id="pageid2"]/table/tbody/tr/td[4]/a/span')
                webdriver.ActionChains(self.browser).move_to_element(next_element).click(next_element).perform()
                # raise scrapy.exceptions.IgnoreRequest(request)
            time.sleep(3)
            return scrapy.http.HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8', status=200)
        except TimeoutException:
            return scrapy.http.HtmlResponse(url=request.url, status=500, request=request)

    def process_response(self, request, response, spider):
        print(request, response)
        return response

    def process_exception(self, request, exception, spider):
        # 至少返回None或者request或者response
        pass


# 爬虫中间件
class CustomSpiderMiddleware(object):
    @ classmethod
    def from_crawler(cls, crawler):
        s = cls() #这是关于扩展需要用的
        return s

    def process_spider_input(self, response, spider):
        # 下载完成之后执行,然后交给parse处理
        return None

    def process_spider_output(self, response, result, spider):
        # spider结果处理
        for i in result:
            if not i['unit']:
                name = i['name']
                i['unit'] = name.split('公司')[0]+'公司' if '公司' in name else name
            yield i

    def process_spider_exception(self, response, exception, spider):
        # 异常调用 继续交给后续中间件处理异常；含 Response 或 Item 的可迭代对象(iterable)，交给调度器或pipeline
        pass

    # 只在爬虫启动时候，只执行一次 读取最开始爬虫start_requests方法中返回生成器的 然后循环在这儿一个个的返回
    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        print('爬虫打开了%s'%spider.name)


# 扩展，用于监听爬虫生命周期活动
class MyExtend(object):
    def __init__(self,crawler):
        self.crawler = crawler
        # 在指定信号上注册操作
        crawler.signals.connect(self.start, scrapy.signals.engine_started)
        crawler.signals.connect(self.close, scrapy.signals.spider_closed)

        # engine_started = object()  # 引擎启动时
        # engine_stopped = object()  # 引擎停止时
        # spider_opened = object()  # 爬虫启动时
        # spider_idle = object()  # 爬虫闲置时
        # spider_closed = object()  # 爬虫停止时
        # spider_error = object()  # 爬虫错误时
        # request_scheduled = object()  # 调度器调度时
        # request_dropped = object()  # 调取器丢弃时
        # response_received = object()  # 得到response时
        # response_downloaded = object()  # response下载时
        # item_scraped = object()  # yield item 时
        # item_dropped = object()  # drop item 时

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def start(self):
        print('开始爬取')

    def close(self):
        print('关闭爬取')
