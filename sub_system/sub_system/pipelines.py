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

<<<<<<< HEAD
=======

>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
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
<<<<<<< HEAD
        info['belong_to']=item['belong_to']
=======
        info['belong_to'] = item['belong_to']
>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
        line = json.dumps(info, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

<<<<<<< HEAD
=======

>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
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
<<<<<<< HEAD
        info['belong_to']=item['belong_to']
=======
        info['belong_to'] = item['belong_to']
>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
        line = json.dumps(info, ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

<<<<<<< HEAD
class flowAreaAPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.FLOW_AREA_A_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        return item



class flowAreaBPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.FLOW_AREA_B_TOPIC, json.dumps(dict(item), ensure_ascii=False))
=======

class flowAreaAPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.FLOW_AREA_A_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item


class flowAreaBPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.FLOW_AREA_B_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        print(item)
>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
        return item


class portableDevicePipeline:
    def __init__(self):
<<<<<<< HEAD
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.PORTABLE_DEVICE_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        return item



class sleetPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.SLEET_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        return item


class device1HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.DEVICE_HISTORY_ONE, json.dumps(dict(item), ensure_ascii=False))
        return item


class device2HistoryPipeline:
    def __init__(self):
        self.kafkaUtils = kafka.KafKaUtils()

    def process_item(self, item, spider):
        self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        return item
=======
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.PORTABLE_DEVICE_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item


class sleetPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.SLEET_TOPIC, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item


class Area12HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item

class Area13HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item

class Area14HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item

class Area15HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item

class Area16HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item


class Area17HistoryPipeline:
    def __init__(self):
        # self.kafkaUtils = kafka.KafKaUtils()
        pass

    def process_item(self, item, spider):
        # self.kafkaUtils.send(kafka.DEVICE_HISTORY_TWO, json.dumps(dict(item), ensure_ascii=False))
        print(item)
        return item
>>>>>>> 550e48a172521ee31e1043de80b03376ee3a3996
