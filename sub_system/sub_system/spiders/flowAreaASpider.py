import scrapy
import re
from ..items import DeviceItem, flowAreaAItem
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import bs4

class FlowAreaASpider(scrapy.Spider):
    name = 'flowAreaASpider'
    allowed_domains = ['159.226.153.63']
    start_urls = ['http://159.226.153.63/collectdata/datacollect_list_A.aspx']
    custom_settings = {
        'ITEM_PIPELINES': {
            'sub_system.pipelines.flowAreaAPipeline': 200
        }
    }

    username = 'fangshan'
    password = '123456'
    cookies = {}

    def __init__(self):
        # 处理免密登录
        browser = webdriver.Firefox()
        browser.get(self.start_urls[0])
        # 输入账号
        browser.find_element_by_xpath(
            '//input[@type="text"]').send_keys(self.username)
        # 输入密码
        browser.find_element_by_xpath(
            '//input[@type="password"]').send_keys(self.password)
        # 点击登陆按钮
        browser.find_element_by_xpath("//input[@class='submit']").click()

        # 获得cookies
        seleniumCookies = browser.get_cookies()
        cookie = [item["name"] + ":" + item["value"]
                  for item in seleniumCookies]
        for elem in cookie:
            str = elem.split(':')
            self.cookies[str[0]] = str[1]
        browser.close()

    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], cookies=self.cookies, callback=self.parseTotalPage, dont_filter=True)

    def parseTotalPage(self, response):
        # 获取总页数
        soup = BeautifulSoup(response.text, "lxml")
        tag = soup.find('div', style='text-align:left; float:left;')
        totalPage = int(re.search(r'/\d+页', tag.string).group(0)[1:-1])
        for i in range(1, totalPage+1):
            url = self.start_urls[0] + '?page=' + str(i)
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parseOnePage, dont_filter=True)

    def parseOnePage(self, response):
        # 获取单个页面中存放数据组件的容器组件
        soup = BeautifulSoup(response.text, "lxml")
        tagTbody = soup.find('tbody')
        for tagTr in tagTbody:
            if type(tagTr) == bs4.NavigableString:
                continue
            yield self.extractData(tagTr)

    def extractData(self, tag):
        # 从数据组件中提取数据
        tagTdList = tag.contents
        item = flowAreaAItem()
        item['id'] = tagTdList[2].string.strip()
        item['name'] = tagTdList[3].string.strip()
        item['deviceId'] = tagTdList[4].string.strip()
        item['date'] = tagTdList[5].string.strip()
        item['time'] = tagTdList[6].string.strip()
        item['flow'] = tagTdList[7].string.strip()
        item['oneFlow'] = tagTdList[8].string.strip()
        item['sandMeasure'] = tagTdList[9].string.strip()
        return item