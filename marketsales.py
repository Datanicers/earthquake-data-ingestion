import pandas as pd
from kafka import KafkaProducer
#from kafka import KafkaConsumer

#producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
df = pd.read_csv("MarketSales.csv",low_memory=False)
df['all_data'] = df[df.columns[0:]].apply(
    lambda x: ','.join(x.dropna().astype(str)),
    axis=1
)
print(len(df['all_data']))
for i in df['all_data']:
     print(i.encode("utf-8"))
     break