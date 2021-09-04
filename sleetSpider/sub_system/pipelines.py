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



class sleetPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.SLEET_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        return item


