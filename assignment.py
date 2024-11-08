# from pymongo import MongoClient
# Client=MongoClient("mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/")
# db=Client['PYTHON']
# collection= db["python_2"]
# data={'name':'vindu','age':22,'mail':'vinay@123','mobil_no':9347668118,'addres':'anantapur'}
# result=collection.insert_one(data)
# print(result.inserted_id)


# from pymongo import MongoClient
# Client=MongoClient('mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/')
# db=Client['TEST']
# collection=db['practice_collection']
# data=[{'name':'vinay','age':22,'mail':'vinay@123','number':9876543211},
#       {'name':'jeethu','age':21,'mail':'jeethu@123','number':9988776655},
#       {'name':'raju','age':23,'mail':'jangam@123','number':8877665544},
#       {'name':'mahesh','age':23,'mail':'mahesh@123','number':7766554433}]
# result=collection.insert_many(data)
# print(result.inserted_ids)


from pymongo import MongoClient
from bson import ObjectId
client=MongoClient('mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/')
db=client['TEST']
collection=db['practice_collection']
# data=[{'name':'vinay','age':22,'mail':'vinay@123','number':9876666666},
#       {'name':'vindu','age':20,'mail':'vindu@123','number':9876555555},
#       {'name':'ashok','age':25,'mail':'ashok@123','number':9876544444},
#       {'name':'vindu','age':22,'mail':'vindu@1233','number':9876543333},
#       {'name':'gaye','age':21,'mail':'gaye@123','number':9876543222}]
# result=collection.insert_many(data)
# print(result.inserted_ids)

document_id=ObjectId('6526034e520ad5ea569a3b34')
result=collection.delete_one({'_id':document_id})
if result.deleted_count==1:
     print(f'Document with _id {document_id} deleted successfully.')
else:
      print(f'No document found with _id {document_id}')

# data={'name':'vindu','age':20}
# collection.delete_one(data)
# print('data  Deleted')

# result=collection.find()
# for i in result:
#     print(i)