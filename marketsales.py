import pandas as pd
from kafka import KafkaProducer
#from kafka import KafkaConsumer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
simple_data = pd.read_excel("MarketSales.xlsx")
#print(simple_data.head())
simple_data['kafka_message'] = simple_data['ID'].astype(str) + "," + \
 simple_data['ITEMCODE'] + "," + simple_data['ITEMNAME'].astype(str) + "," + \
 simple_data['FICHENO'] + "," + simple_data['DATE_'] + "," + \
 simple_data['AMOUNT'].astype(str) + simple_data['PRICE'].astype(str) + "," + simple_data['LINENETTOTAL'].astype(str) + ","+ simple_data['LINENET'].astype(str) + ","
+ simple_data['BRANCHNR'].astype(str) + ","+ simple_data['BRANCH'].astype(str) + ","+ simple_data['SALESMAN'].astype(str) + ","+ simple_data['CITY'].astype(str) + ","
+ simple_data['REGION'].astype(str) + ","+ simple_data['LATITUDE'].astype(str) + ","+ simple_data['CLIENTNAME'].astype(str) + ","
+ simple_data['BRAND'].astype(str) + ","+ simple_data['CATEGORY_NAME1'].astype(str)+ simple_data['CATEGORY_NAME2'].astype(str) + ","+ simple_data['CATEGORY_NAME3'].astype(str)
+ simple_data['STARTDATE'].astype(str) + ","+ simple_data['ENDDATE'].astype(str) + simple_data['GENDER'].astype(str)

for index, row in simple_data.iterrows():
    producer.send('earthquake', key=str(row[0]).encode(), value=row[-1].encode())
