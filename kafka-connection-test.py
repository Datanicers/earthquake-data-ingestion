import kafka


consumer = kafka.KafkaConsumer(bootstrap_servers=['35.188.88.209:9092'])
topics = consumer.topics()
print(topics)
if not topics:
    raise RuntimeError()


from kafka import KafkaProducer
# Create a producer object
# Ip can be different in your case
producer = KafkaProducer(bootstrap_servers=['35.188.88.209:9092'])
# Basit bir mesajın oluşturulması ve gönderilmesi
# Asynchronous varsayılan
# b string'i byte'a çevirmek için
# deneme topic adı
producer.send('earthQuakeTopic', b'python producer ile gonderildi')
producer.flush()
producer.close()