# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class sleetItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 监测点名称
    deviceId = scrapy.Field() # 设备编号
    date = scrapy.Field() # 监测日期
    longitude = scrapy.Field()  # 经度
    latitude = scrapy.Field()  # 纬度
    temperature = scrapy.Field() # 温度
    humidity = scrapy.Field() # 湿度
    rainSnow = scrapy.Field() # 降雨雪量
    duration = scrapy.Field() # 时长