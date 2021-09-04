# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 天航佳德所有的数据项都一样
class HistoryItem(scrapy.Item):
    id = scrapy.Field()  # 编号
    date = scrapy.Field()  # 日期
    sandMeasureId = scrapy.Field()  # 泥沙测量编号
    genFlowSpace = scrapy.Field()  # 产流体积
    sandContent = scrapy.Field()  # 泥沙含量
    drySandLoss = scrapy.Field()  # 干泥沙流失量
    rainfall = scrapy.Field()  # 雨量
    runoffWeight = scrapy.Field()  # 产流重量
    runoffDensity = scrapy.Field()  # 径流密度
    deviceV = scrapy.Field()  # 设备电压
    errorCode = scrapy.Field()  # 故障码
    deviceId = scrapy.Field() # 辨别是哪一个设备
