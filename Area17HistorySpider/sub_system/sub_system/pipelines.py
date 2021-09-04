# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import json
import sub_system.kafka_utils as kafka
from collections import Counter

class Area13HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.AREA13, json.dumps(dict(item), ensure_ascii=False))
        item['deviceId'] = 5
        return item

class Area14HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.AREA14, json.dumps(dict(item), ensure_ascii=False))
        item['deviceId'] = 6
        return item

class Area15HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.AREA15, json.dumps(dict(item), ensure_ascii=False))
        item['deviceId'] = 7
        return item

class Area16HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.AREA16, json.dumps(dict(item), ensure_ascii=False))
        item['deviceId'] = 8
        return item


class Area17HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.AREA17, json.dumps(dict(item), ensure_ascii=False))
        item['deviceId'] = 9
        return item
