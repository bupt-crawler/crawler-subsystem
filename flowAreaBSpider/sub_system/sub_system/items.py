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

class flowAreaAItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 观测点名称
    deviceId = scrapy.Field() # 设备编号
    date = scrapy.Field() # 监测日期
    time = scrapy.Field() # 检测时间
    flow = scrapy.Field() # 径流量
    oneFlow = scrapy.Field() # 单次测试流量
    sandMeasure = scrapy.Field() # 含沙量

class flowAreaBItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 观测点名称
    deviceId = scrapy.Field() # 设备编号
    date = scrapy.Field() # 监测日期
    time = scrapy.Field() # 检测时间
    flow = scrapy.Field() # 径流量
    oneFlow = scrapy.Field() # 单次测试流量
    sandMeasure = scrapy.Field() # 含沙量

class portableDeviceItem(scrapy.Item):
    id = scrapy.Field() # 序号
    name = scrapy.Field() # 监测点名字
    deviceId = scrapy.Field() # 设备编号
    projectId = scrapy.Field() # 工程编号
    date = scrapy.Field() # 检测日期
    longitude = scrapy.Field() # 经度
    latitude = scrapy.Field() # 纬度
    sandMeasure = scrapy.Field() # 含沙量

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
