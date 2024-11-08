from pymongo import MongoClient
from bson import ObjectId
client=MongoClient('mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/')
db=client['VINDU']
collection_1=db['vindu_1']
collection_2=db['vindu_2']
data=[{'name':'vinay','age':23,'gender':'male','place':'pamudurthi'},
      {'name':'jeethu','age':21,'gender':'female','place':'ramagari'},
       {'name':'ashok','age':25,'gender':'male','place':'kadiri'}]
asd=[{'name':'raju','age':24,'number':'0987654321'},
      {'name':'mahesh','age':25,'number':'9876543210'}]
result_1=collection_1.insert_many(data)
result_2=collection_2.insert_many(asd)
# print(result_1.inserted_ids)
# print(result_2.inserted_ids)
result_3=collection_1.find()
j=1
for i in result_3:
    print(f"Entry {j}:",i)
    j=j+1


