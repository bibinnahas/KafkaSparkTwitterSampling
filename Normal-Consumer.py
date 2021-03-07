from json import loads
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'covid_tweets',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

for message in consumer:
    print(f"{message.value}")
