# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class portableDeviceItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 监测点名字
    deviceId = scrapy.Field() # 设备编号
    projectId = scrapy.Field() # 工程编号
    date = scrapy.Field() # 检测日期
    longitude = scrapy.Field() # 经度
    latitude = scrapy.Field() # 纬度
    sandMeasure = scrapy.Field() # 含沙量