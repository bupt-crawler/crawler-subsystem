# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class flowAreaAItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 观测点名称
    deviceId = scrapy.Field() # 设备编号
    date = scrapy.Field() # 监测日期
    time = scrapy.Field() # 检测时间
    flow = scrapy.Field() # 径流量
    oneFlow = scrapy.Field() # 单次测试流量
    sandMeasure = scrapy.Field() # 含沙量
