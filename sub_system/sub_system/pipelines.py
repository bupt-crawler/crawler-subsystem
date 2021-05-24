# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
from collections import Counter


class DevicePipeline:
    def __init__(self):
        self.file = codecs.open('device_data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        info = {}
        info['name'] = item['name']
        info['id'] = item['id']
        info['phone'] = item['phone']
        info['type'] = item['type']
        info['model'] = item['model']
        info['location'] = item['location']
        info['photo'] = item['photo']
        info['belong_to']=item['belong_to']
        line = json.dumps(info, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class SubSystemPipeline:
    def __init__(self):
        self.file = codecs.open('Json_data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        info = {}
        info['name'] = item['name']
        info['id'] = item['id']
        info['phone'] = item['phone']
        info['type'] = item['type']
        info['model'] = item['model']
        info['location'] = item['location']
        info['photo'] = item['photo']
        info['belong_to']=item['belong_to']
        line = json.dumps(info, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class flowAreaAPipeline:
    def __init__(self):
        self.file = codecs.open('flowAreaA.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()

class flowAreaBPipeline:
    def __init__(self):
        self.file = codecs.open('flowAreaB.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()

class portableDevicePipeline:
    def __init__(self):
        self.file = codecs.open('portableDevice.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()

class sleetPipeline:
    def __init__(self):
        self.file = codecs.open('sleet.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()

class device1HistoryPipeline:
    def __init__(self):
        self.file = codecs.open('device1History.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()

class device2HistoryPipeline:
    def __init__(self):
        self.file = codecs.open('device2History.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item

    def spider_closed(self, spider):
        self.file.close()