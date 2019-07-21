# coding:utf-8

from .crawler import Crawler
from .redis_client import RedisClient

FULL_COUNT = 2000


class Getter:

    def __init__(self):
        self.redis_client = RedisClient()
        self.crawler = Crawler()

    @property
    def is_full(self):
        """
            判断代理池是否满了
        """
        if self.redis_client.get_proxy_count() >= FULL_COUNT:
            return True
        else:
            return False

    def run(self):
        """
            将爬取到的代理存入redis
        """
        if not self.is_full:
            proxy_list = self.crawler.get_crawler_proxy()
            for proxy in proxy_list:
                self.redis_client.add(proxy)
