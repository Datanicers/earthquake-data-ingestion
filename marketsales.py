import pandas as pd
from kafka import KafkaProducer
#from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
df = pd.read_csv("/home/beytullah557/MarketSales_(1).csv",low_memory=False)
df['all_data'] = df[df.columns[0:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)

for i in df['all_data']:
    producer.send('marketsales', i.encode("utf-8"))