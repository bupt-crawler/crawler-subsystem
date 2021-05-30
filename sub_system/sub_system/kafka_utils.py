from kafka import KafkaProducer

KAFKA_HOST = '112.98.239.146:9092'
DEVICE_HISTORY_ONE = 'device_history_one'
DEVICE_HISTORY_TWO = 'device_history_two'
FLOW_AREA_A_TOPIC = 'flow_area_a'
FLOW_AREA_B_TOPIC = 'flow_area_b'
PORTABLE_DEVICE_TOPIC = 'portable_device'
SLEET_TOPIC = 'sleet'


# producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)

class KafKaUtils:
    producer = KafkaProducer(bootstrap_servers=KAFKA_HOST)

    def send(self, topic, value, key=None):
        k, v = None, None
        if k is not None:
            k = str.encode(key)
        v = str.encode(value)
        future = self.producer.send(topic, v, k, partition=0)
        return future.get(timeout=10)

# def send(producer, topic, value, key=None):
#     k, v = None, None
#     if k is not None:
#         k = str.encode(key)
#     v = str.encode(value)
#     future = producer.send(topic, v, k, partition=0)
#     return future.get(timeout=10)


# flow_area_a = open('../flowAreaA.json', 'r', encoding='utf-8')
# for line in flow_area_a:
#     send(FLOW_AREA_A_TOPIC, line)
# flow_area_a.close()
#
# flow_area_b = open('../flowAreaB.json', 'r', encoding='utf-8')
# for line in flow_area_b:
#     send(FLOW_AREA_B_TOPIC, line)
# flow_area_b.close()
#
# portable_device = open('../portableDevice.json', 'r', encoding='utf-8')
# for line in portable_device:
#     send(PORTABLE_DEVICE_TOPIC, line)
# portable_device.close()
#
# sleet = open('../sleet.json', 'r', encoding='utf-8')
# for line in sleet:
#     send(SLEET_TOPIC, line)
# sleet.close()
