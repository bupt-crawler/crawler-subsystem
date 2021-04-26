import scrapy
import re

from scrapy.http.request import Request
from ..items import DeviceItem
from selenium import webdriver


class MainSpiderSpider(scrapy.Spider):
    name = 'main_spider'
    allowed_domains = ['159.226.153.63']
    start_urls = ['http://159.226.153.63/LogIn.aspx',
                  'http://159.226.153.63/baseinfo/posm_list.aspx']
    count = 1
    username = 'fangshan'
    password = '123456'
    base_url = 'http://159.226.153.63'
    device_num = 0

    def start_requests(self):
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
        cookMap = {}
        for elem in cookie:
            str = elem.split(':')
            cookMap[str[0]] = str[1]

      #  browser.close()
        yield scrapy.FormRequest(self.start_urls[1], cookies=cookMap, callback=self.parseDevicePage, dont_filter=True)

    def parseAllPages(self, response):
        # Crawl device page
        scrapy.Request(self.base_url+'/baseinfo/posm_list.aspx',
                       callback=self.parseDevicePage, dont_filter=True, errback=self.errback)

    def errback(self, failure):
        self.logger.error(repr(failure))

    def parseDevicePage(self, response):
        rows = response.xpath('//table[@class="gv"]/tbody/text()').extract()
        cnt = 0
        for row in rows:
            cnt += 1
            # 注意要在td前面加上"./"，表示此td是node_list的下一级
            name = row.xpath('./td[1]/text()').extract()
            id = row.xpath('./td[2]/text()').extract()
            phone = row.xpath('./td[3]/text()').extract()
            type = row.xpath('./td[4]/text()').extract()
            model = row.xpath('./td[5]/text()').extract()
            position = row.xpath('./td[6]/text()').extract()
            image_url = row.xpath('./td[7]/text()').extract()
            belong_to = row.xpath('./td[8]/text()').extract()
            device_info = DeviceItem()
            device_info['name'] = name if name else ""
            device_info['id'] = id if id else ""
            device_info['phone'] = phone if phone else ""
            device_info['type'] = type if type else ""
            device_info['model'] = model if model else ""
            device_info['position'] = position if position else ""
            device_info['image_url'] = image_url if image_url else ""
            device_info['belong_to'] = belong_to if belong_to else ""
            yield device_info

        self.device_num += cnt
        total_idx = response.xpath(
            '//div[@class="form-inline"]/div[@style="text-align:left; float:left"]/text()').extract()
        re.findall(r'[/](\d+?)[页]', total_idx)

        next_url = self.base_url+'/baseinfo/posm_list.aspx?page='+1
        yield scrapy.Request(next_url, callback=self.parseDevicePage)
