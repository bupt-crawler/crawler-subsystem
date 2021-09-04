from kafka import KafkaProducer

KAFKA_HOST = '112.98.239.146:9092'
PORTABLE_DEVICE_TOPIC = 'portable_device'


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



