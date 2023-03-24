from kafka import KafkaProducer
import time
import requests
import json

API_URL = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
producer = KafkaProducer(bootstrap_servers = ['34.132.165.75'],value_serializer=lambda x: json.dumps(x).encode('utf-8'))
while True:
    response = requests.get(API_URL, stream=True)
    data=response.json()
    try :
        for line in data:
                producer.send('depremTopic', value=line)
                producer.flush()
    except Exception as e:
        print("Error")

  #  time.sleep(1)