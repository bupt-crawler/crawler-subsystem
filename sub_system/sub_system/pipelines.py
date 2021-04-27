# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.conf import settings
import codecs
import json
from collections import Counter

class JsonPipeline(object):
    def __init__(self):
        self.file = codecs.open('Json_data.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # print("*****************************")
        # print(type(item))
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
        print("保存成功")
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class SubSystemPipeline:
    def process_item(self, item, spider):
        return item
