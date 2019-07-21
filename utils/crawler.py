# coding:utf-8

import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time

"""
    爬取代理网站的免费代理并返回
"""

cookie_66 = 'gsScrollPos-3382=0; gsScrollPos-332=; __jsluid_h=394333cddd10c5fb8d127e11771bc5b4; Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1562396517; __jsl_clearance=1562685395.32|0|AEtkA33BWM0Xu7LlrjJ2ynqRIPo%3D; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1562685398'
cookie_xici = '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWJmNzFkYmY3ZjVkNWRiZGM0NjFkMjdlNzQ0NWM0NWE5BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMVgySG9Lc0xGclpCZHlDWUdwVXAvY1p1cVlLbUlXeHJoY1JJMkJia0pnRUk9BjsARg%3D%3D--a468129b594b386a47b847765029ea77733ae1c3; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1563550705; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1563550705'
cookie_kuai = 'channelid=0; sid=1563549282094288; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1563550931; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1563550931; _ga=GA1.2.2041047130.1563550931; _gid=GA1.2.2046439716.1563550931; _gat=1'

class Crawler:

    def get_crawler_proxy(self):
        proxy_list_xici = self.crawl_xici()
        proxy_list_66 = self.crawl_66()
        proxy_list_kuaidaili = self.crawl_kuaidaili()
        return proxy_list_xici + proxy_list_66 + proxy_list_kuaidaili

    def crawl_66(self):
        """爬取66代理
        """
        print('爬取66代理......')
        proxies = set()
        for i in range(1, 35):
            print(i)
            url = 'http://www.66ip.cn/areaindex_' + str(i) + '/1.html'
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                'Host': 'www.66ip.cn',
                'Cookie': cookie_66,
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
            }

            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, 'html.parser')
            items = soup.select('.footer table tr')
            for i in range(1, len(items)):
                tds = items[i].select('td')
                ip = tds[0].string
                port = tds[1].string
                proxy = ip + ':' + port
                if proxy:
                    # print(proxy.replace(' ', ''))
                    proxies.add(proxy)
        return list(proxies)

    def crawl_xici(self):
        """爬取西刺代理
        """
        print('爬取西刺代理......')
        proxy_list = []
        for i in range(1, 20):
            try:
                url = 'http://www.xicidaili.com/nn/' + str(i)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'www.xicidaili.com',
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                    'Cookie': cookie_xici
                }

                res = requests.get(url, headers=headers)
                if res.status_code == 200:
                    doc = pq(res.text)
                    for odd in doc('.odd').items():
                        info_list = odd.find('td').text().split(' ')
                        # print(info_list)
                        if len(info_list) == 11:
                            proxy = info_list[1].strip() + ':' + info_list[2].strip()
                            proxy = proxy.replace(' ', '')
                            proxy_list.append(proxy)
            except Exception as e:
                continue
        print('爬取到西刺代理 %s 个' % len(proxy_list))
        return proxy_list
    
    def crawl_kuaidaili(self):
        """爬取快代理
        """
        print('爬取快代理......')
        proxies = set()
        for i in range(1, 50):
            try:
                url = 'https://www.kuaidaili.com/free/inha/' + str(i)
                time.sleep(1)
                headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                    'Host': 'www.kuaidaili.com',
                    # 'Referer': 'http://www.66ip.cn/',
                    'Cookie': cookie_kuai,
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
                }

                res = requests.get(url, headers=headers)
                soup = BeautifulSoup(res.text, 'html.parser')
                items = soup.select('#list tbody tr')
                for item in items:
                    tds = item.select('td')
                    ip = tds[0].string
                    port = tds[1].string
                    proxy = ip + ':' + port
                    if proxy:
                        proxies.add(proxy.replace(' ', ''))
            except Exception as e:
                continue
        print('爬取到块代理 %s 个' % len(proxies))
        return list(proxies)

if __name__ == "__main__":
    c = Crawler()
    #c.crawl_66()
    # c.crawl_xici()
    c.crawl_kuaidaili()
