from pymongo import MongoClient
from bson import ObjectId
client=MongoClient('mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net')
db=client['ASSESSMENT']
collection=db['assessment_1']
# collection=db['assessment_2']
# data=[{'name':'vinay','age':23,'gender':'male','place':'pamudurthi'},
#       {'name':'jeethu','age':21,'gender':'female','place':'ramagari'},
#       {'name':'ashok','age':25,'gender':'male','place':'kadiri'}]
# result=collection.insert_many(data)
# print(result.inserted_ids)

# data=[{'name':'raju','age':24,'number':'0987654321'},
#       {'name':'mahesh','age':25,'number':'9876543210'}]
# result=collection.insert_many(data)
# print(result.inserted_ids)

# filter={'name':'vinay'}
# update={'$set':{'name':'vindu'}}
# collection.update_one(filter,update)

# result=collection.find()
# for i in result:
#     print(i)

document_id=ObjectId('6527e699ddbf4cdaf4eadc70')
result=collection.delete_one({'_id':document_id})
