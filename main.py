from kafka import KafkaProducer
import time
import json
import requests
from flask import Flask

API_URL = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
producer = KafkaProducer(bootstrap_servers = ['35.188.88.209:9092'],value_serializer=lambda x: json.dumps(x).encode('utf-8'))

response = requests.get(API_URL, stream=True)
data=response.json()

for line in data:
        producer.send('earthQuakeTopic', value=line)
        producer.flush()
        print("sent")


  #  time.sleep(1)