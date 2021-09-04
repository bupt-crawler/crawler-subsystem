import scrapy
import json
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver

from sub_system.items import HistoryItem
from selenium.webdriver.firefox.options import Options
from sub_system.settings import *


class Area13historyspiderSpider(scrapy.Spider):
    name = 'Area13HistorySpider'
    allowed_domains = ['gprs.sj2000.org']
    start_urls = ['http://gprs.sj2000.org/Web/TDDataManage.aspx?type=2&EquipmentID=2863']
    custom_settings = {
        'ITEM_PIPELINES': {
            'sub_system.pipelines.Area13HistoryPipeline': 200
        }
    }
    oldtime = ''  # 本地存储的最新时间
    newtime = ''  # 记录爬取的所有数据中最新的时间
    timeName = "Area13HistoryTime"  # 时间字典中的key
    dictime = {}  # 从本地文件中获取到的时间字典

    def __init__(self, **kwargs):
        try:
            # 免密登录
            url = "http://gprs.sj2000.org/Login.aspx"
            username = TIANHANG_USER
            password = TIANHANG_PASSWORD

            # 浏览器不可视，用于在服务器运行
            options = webdriver.FirefoxOptions()
            options.set_headless()
            self.browser = webdriver.Firefox(firefox_options=options,
                                             executable_path=DRIVER_WINDOWS)

            # 浏览器可视，便于调试
            # self.browser = webdriver.Firefox(executable_path= DRIVER_WINDOWS)

            self.browser.get(url)
            # 输入账号
            self.browser.find_element_by_xpath(
                '//input[@type="text"]').send_keys(username)
            # 输入密码
            self.browser.find_element_by_xpath(
                '//input[@class="mm"]').send_keys(password)
            # 点击登陆按钮
            self.browser.find_element_by_xpath("//input[@id='btnLogin']").click()
            self.getOldtime()
        except:
            self.browser.quit()

    def start_requests(self):
        yield scrapy.FormRequest(self.start_urls[0], callback=self.browserfun)

    def browserfun(self, response):
        try:
            # 模拟浏览器操作:选择开始日期，点击查询按钮，使数据显示在表格中
            self.browser.get(self.start_urls[0])
            # 点击日期选择
            imgBt = self.browser.find_element_by_xpath(
                "//img[@src=\"data:image/gif;base64,R0lGODlhAQABAID/AMDAwAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==\"]")
            self.clickAnElement(imgBt)
            time.sleep(1)
            # 点击年和月选择
            yearAndMonthBt = self.browser.find_element_by_xpath("//button[@class=\" x-btn-text\"]")
            self.clickAnElement(yearAndMonthBt)
            time.sleep(1)
            # 选择2018年,一个较早的年份
            tdList = self.browser.find_elements_by_tag_name('td')
            tdyear2018 = 0
            for td in tdList:
                if td.text == '2018':
                    tdyear2018 = td
                    break
            self.clickAnElement(tdyear2018)
            time.sleep(1)
            # 点击确定，选择年月完毕
            okBt = self.browser.find_element_by_xpath("//button[@class=\"x-date-mp-ok\"]")
            self.clickAnElement(okBt)
            time.sleep(1)
            # 选择日历上的第一项
            a = self.browser.find_element_by_xpath("//a[@class=\"x-date-date\"]")
            self.clickAnElement(a)
            time.sleep(1)
            # 点击查询按钮
            submitBt = self.browser.find_element_by_xpath("//button[@class=\' x-btn-text icon-pagefind\']")
            self.clickAnElement(submitBt)
            time.sleep(1)
            # 获取下一页按钮
            nextpageBt = self.browser.find_element_by_xpath("//button[@class=\' x-btn-text x-tbar-page-next\']")
            # 获取总页数
            l = self.browser.find_elements_by_class_name('xtb-text')
            page = int(re.search(r'共 \d+ 页', l[1].text).group(0)[2:-2])
            # 获取刷新按钮
            refresh = self.browser.find_element_by_xpath("//button[@class=\' x-btn-text x-tbar-loading\']")
            # 一页一页的处理数据
            for i in range(page):
                time.sleep(0.5)
                itemList = self.extractData()
                # 如果没取到数据，就刷新网页
                while len(itemList) == 0:
                    self.clickAnElement(refresh)
                    itemList = self.extractData()
                # 从数据列表中yield Item
                oldData = False
                for item in itemList:
                    # 当数据为新数据时才获取
                    if item['date'] > self.oldtime:
                        if item['date'] > self.newtime:
                            self.newtime = item['date']
                        yield item
                    # 当数据为老数据时，不获取
                    else:
                        oldData = True
                        break
                # 如果当前页面获取到的数据已经为老数据，就不再继续往下翻页获取了
                if oldData == True:
                    break
                self.clickAnElement(nextpageBt)
        finally:
            self.browser.quit()

    def extractData(self):
        # 从浏览器数据表格中提取数据
        idlist = []  # 编号
        datelist = []  # 日期
        sandMeasurIdlist = []  # 泥沙测量编号
        genFlowSpacelist = []  # 产流体积
        sandContentlist = []  # 泥沙含量
        drySandLosslist = []  # 干泥沙流失量
        rainFalllist = []  # 雨量
        runoffWeightlist = []  # 产流重量
        runoffDensitylist = []  # 径流密度
        deviceVlist = []  # 设备电压
        errorCodelist = []  # 故障码
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        # 获取idlist
        idTagList = soup.find_all('div', class_="x-grid3-cell-inner x-grid3-col-numberer")
        for idTag in idTagList:
            idlist.append(idTag.string)
        # 获取日期
        dateTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-1')
        for dateTag in dateTagList:
            datelist.append(dateTag.string)
        # 获取泥沙测量编号
        sandMeasurIdTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou0')
        for sandMeasurIdTag in sandMeasurIdTagList:
            sandMeasurIdlist.append(sandMeasurIdTag.string)
        # 获取产流体积
        genFlowSpaceTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou1')
        for genFlowSpaceTag in genFlowSpaceTagList:
            genFlowSpacelist.append(genFlowSpaceTag.string)
        # 获取泥沙含量
        sandContentTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou2')
        for sandContentTag in sandContentTagList:
            sandContentlist.append(sandContentTag.string)
        # 获取干泥沙流失量
        drySandLossTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou3')
        for drySandLossTag in drySandLossTagList:
            drySandLosslist.append(drySandLossTag.string)
        # 获取雨量
        rainFallTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou4')
        for rainFallTag in rainFallTagList:
            rainFalllist.append(rainFallTag.string)
        # 获取产流重量
        runoffWeightTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou5')
        for runoffWeightTag in runoffWeightTagList:
            runoffWeightlist.append(runoffWeightTag.string)
        # 获取径流密度
        runoffDensityTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou6')
        for runoffDensityTag in runoffDensityTagList:
            runoffDensitylist.append(runoffDensityTag.string)
        # 获取设备电压
        deviceVTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou7')
        for deviceVTag in deviceVTagList:
            deviceVlist.append(deviceVTag.string)
        # 获取故障码
        errorCodeTagList = soup.find_all('div', class_='x-grid3-cell-inner x-grid3-col-DataJzHou8')
        for errorCodeTag in errorCodeTagList:
            errorCodelist.append(errorCodeTag.string)
        itemList = []
        for index in range(len(idlist)):
            item = HistoryItem()
            item['id'] = idlist[index]
            item['date'] = datelist[index]
            item['sandMeasureId'] = sandMeasurIdlist[index]
            item['genFlowSpace'] = genFlowSpacelist[index]
            item['sandContent'] = sandContentlist[index]
            item['drySandLoss'] = drySandLosslist[index]
            item['rainfall'] = rainFalllist[index]
            item['runoffWeight'] = runoffWeightlist[index]
            item['runoffDensity'] = runoffDensitylist[index]
            item['deviceV'] = deviceVlist[index]
            item['errorCode'] = errorCodelist[index]
            itemList.append(item)
        return itemList

    def clickAnElement(self, bt):
        # 因为网页是动态生成的，有时会出现元素点击异常。当出现异常时等待一段时间后再次点击
        try:
            bt.click()
        except:
            time.sleep(2)
            bt.click()

    def close(spider, reason):
        # 爬虫关闭时更新时间
        spider.updateNewTime()

    def getOldtime(self):
        # 从本地文件中获取oldtime
        file = open(TIME_FILE_TIANHANG, 'r', encoding='utf-8')
        self.dictime = json.load(file)
        self.oldtime = self.dictime[self.timeName]
        self.newtime = self.oldtime
        file.close()

    def updateNewTime(self):
        # 更新本地文件时间记录
        file = open(TIME_FILE_TIANHANG, 'w', encoding='utf-8')
        self.dictime[self.timeName] = self.newtime
        file.write(json.dumps(self.dictime))
        file.close()
