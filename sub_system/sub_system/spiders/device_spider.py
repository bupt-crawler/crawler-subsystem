
import scrapy
import re

from scrapy.http.request import Request
from ..items import DeviceItem
from selenium import webdriver
from ..pipelines import SubSystemPipeline
from selenium.webdriver.firefox.options import Options

class DeviceSpider(scrapy.Spider):

    name = 'device_spider'
    custom_settings={
        'ITEM_PIPELINES':{
          'sub_system.pipelines.DevicePipeline': 200
        }
    }
    allowed_domains = ['159.226.153.63']
    start_urls = ['http://159.226.153.63/baseinfo/posm_list.aspx']
    callback_func=[] #与start_url对应的回调函数
    username = 'fangshan'
    password = '123456'
    login_url = 'http://159.226.153.63/LogIn.aspx'

    device_num_info_raw = ''  # 设备页面原始信息 (“总**页”)
    device_total_idx = 0  # 设备页面的页数
    cookies = {}
    
    def __init__(self, **kwargs):
        options = webdriver.FirefoxOptions()
        options.set_headless()
        browser=webdriver.Firefox(firefox_options=options,executable_path='/usr/bin/geckodriver')

        # browser = webdriver.Firefox('/home/lighthouse/crawler-subsystem/sub_system/')
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
        self.callback_func.append(self.startParseDevicePages)

    def start_requests(self):
        # 开始爬取所有页面
        for i in range(len(self.start_urls)):
            yield scrapy.FormRequest(self.start_urls[i], cookies=self.cookies, callback=self.callback_func[i], dont_filter=True)
      

    def startParseDevicePages(self, response):
        # 获得设备页面总数
        self.device_num_info_raw = response.xpath('//div[@class="form-inline"]/div[@style="text-align:left; float:left;"]/text()').extract()[0]
        self.device_total_idx = int(re.findall(
            r'[/](\d+?)[页]', self.device_num_info_raw)[0])

        for idx in range(int(self.device_total_idx)):
            next_url = self.start_urls[0]+'?page='+str(idx+1)
            yield scrapy.Request(next_url, callback=self.parseDevicePage)


    def errback(self, failure):
        self.logger.error(repr(failure))

    def __eliminateSpace(self,text):
        return re.sub('\s+','',text).strip()

    # def parseDevice(self,response):

    def parseDevicePage(self, response):
        rows = response.xpath('//table[@class="gv"]/tbody/tr')
        for row in rows:
            # 注意要在td前面加上"./"，表示此td是node_list的下一级
            name = self.__eliminateSpace(row.xpath('./td[2]/text()').extract_first())
            id = self.__eliminateSpace(row.xpath('./td[3]/text()').extract_first())
            phone = self.__eliminateSpace(row.xpath('./td[4]/text()').extract_first())
            type = self.__eliminateSpace(row.xpath('./td[5]/text()').extract_first())
            model = self.__eliminateSpace(row.xpath('./td[6]/text()').extract_first())
            position=self.__eliminateSpace(row.xpath('./td[7]/text()').extract_first())
            image_url = self.__eliminateSpace(row.xpath('./td[8]/text()').extract_first())
            belong_to = self.__eliminateSpace((row.xpath('./td[9]/text()').extract_first()))
            device_info = DeviceItem()
            device_info['name'] = name if name else ""
            device_info['id'] = id if id else ""
            device_info['phone'] = phone if phone else ""
            device_info['type'] = type if type else ""
            device_info['model'] = model if model else ""
            device_info['location'] = position if position else ""
            device_info['photo'] = image_url if image_url else ""
            device_info['belong_to'] = belong_to if belong_to else ""
            yield device_info

        # cur_idx = re.findall(r'[,](\d+?)[/]', self.device_num_info_raw)[0]
        # if int(cur_idx) < self.device_total_idx:
        #     next_url = self.start_urls[1]+'?page='+cur_idx
        #     yield scrapy.Request(next_url, callback=self.parseDevicePage)
