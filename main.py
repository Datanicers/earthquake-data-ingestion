from kafka import KafkaProducer
import time
import requests
import json

producer = KafkaProducer(bootstrap_servers = ['34.132.165.75'],value_serializer=lambda x: json.dumps(x).encode('utf-8'))
while True:
    api_url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"
    response = requests.get(api_url, stream=True)
    data=response.json()
    try :
        for line in data:
                producer.send('depremTopic', value=line)
    except Exception as e:
        print("Error")

  #  time.sleep(1)