# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SubSystemItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DeviceItem(scrapy.Item):
    name=scrapy.Field() # 监测站名名称
    id=scrapy.Field() # 设备编号
    phone=scrapy.Field() #手机卡号
    type=scrapy.Field() # 监测站类型
    model=scrapy.Field() #径流量计算模型
    location=scrapy.Field() #设备位置
    photo=scrapy.Field() #现场照片
    belong_to=scrapy.Field() #所属监测站


