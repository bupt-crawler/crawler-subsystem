# encoding: utf-8
import json
import scrapy
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import bs4

from sub_system.items import sleetItem
from sub_system.settings import *

class SleetSpider(scrapy.Spider):
    name = 'sleetSpider'
    allowed_domains = ['159.226.153.63']
    start_urls = ['http://159.226.153.63/collectdata/sleet.aspx']
    custom_settings = {
        'ITEM_PIPELINES': {
            'sub_system.pipelines.sleetPipeline': 200
        }
    }

    username = SANZHI_USER
    password = SANZHI_PASSWORD
    cookies = {}
    oldtime = ''  # 本地存储的最新时间
    newtime = ''  # 记录爬取的所有数据中最新的时间
    timeName = "sleetTime"  # 时间字典的key
    dictime = {}  # 从本地文件中获取到的时间字典

    def __init__(self, **kwargs):
        try:
            # 处理免密登录
            options = webdriver.FirefoxOptions()
            options.set_headless()
            self.browser = webdriver.Firefox(firefox_options=options, executable_path=DRIVER_LINUX)
            self.browser.get(self.start_urls[0])
            # 输入账号
            self.browser.find_element_by_xpath(
                '//input[@type="text"]').send_keys(self.username)
            # 输入密码
            self.browser.find_element_by_xpath(
                '//input[@type="password"]').send_keys(self.password)
            # 点击登陆按钮
            self.browser.find_element_by_xpath("//input[@class='submit']").click()

            # 获得cookies
            seleniumCookies = self.browser.get_cookies()
            cookie = [item["name"] + ":" + item["value"]
                      for item in seleniumCookies]
            for elem in cookie:
                str = elem.split(':')
                self.cookies[str[0]] = str[1]
            self.getOldtime()
        finally:
            self.browser.quit()

    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], cookies=self.cookies, callback=self.parseTotalPage,
                                 dont_filter=True)

    def parseTotalPage(self, response):
        # 获取总页数
        soup = BeautifulSoup(response.text, "lxml")
        tag = soup.find('div', style='text-align:left; float:left;')
        totalPage = int(re.search(r'/\d+页', tag.string).group(0)[1:-1])
        for i in range(1, totalPage + 1):
            url = self.start_urls[0] + '?page=' + str(i)
            yield scrapy.FormRequest(url, cookies=self.cookies, callback=self.parseOnePage, dont_filter=True,priority=totalPage-i+1)

    def parseOnePage(self, response):
        # 获取单个页面中存放数据组件的容器组件
        soup = BeautifulSoup(response.text, "lxml")
        tagTbody = soup.find('tbody')
        for tagTr in tagTbody:
            if type(tagTr) == bs4.NavigableString:
                continue
            item = self.extractData(tagTr)
            if item == None:
                break
            yield item

    def extractData(self, tag):
        # 从数据组件中提取数据
        tagTdList = tag.contents
        item = sleetItem()
        # 该类数据的id不唯一（每页都重置一次），爬取id无意义
        # item['id'] = tagTdList[2].string.strip()
        item['name'] = tagTdList[3].string.strip()
        item['deviceId'] = tagTdList[4].string.strip()
        item['date'] = tagTdList[5].string.strip()
        item['longitude'] = tagTdList[6].string.strip()
        item['latitude'] = tagTdList[7].string.strip()
        item['temperature'] = tagTdList[8].string.strip()
        item['humidity'] = tagTdList[9].string.strip()
        item['rainSnow'] = tagTdList[10].string.strip()
        item['duration'] = tagTdList[11].string.strip()
        nowtime = item['date']
        if nowtime > self.oldtime:
            if nowtime > self.newtime:
                self.newtime = nowtime
            return item
        else:
            return None

    def close(spider, reason):
        # 爬虫关闭时更新时间
        spider.updateNewTime()

    def getOldtime(self):
        # 从本地文件中获取oldtime
        file = open(TIME_FILE, 'r', encoding='utf-8')
        self.dictime = json.load(file)
        self.oldtime = self.dictime[self.timeName]
        self.newtime = self.oldtime
        file.close()

    def updateNewTime(self):
        # 更新本地文件时间记录
        file = open(TIME_FILE, 'w', encoding='utf-8')
        self.dictime[self.timeName] = self.newtime
        file.write(json.dumps(self.dictime))
        file.close()