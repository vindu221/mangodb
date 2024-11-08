from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/")
# db = client['TEST']
# collection = db['practice_collection']
# data = {"name":"vinay","age":22}
# result=collection.insert_one(data)
# print(result.inserted_id)


# data =  [{"name": "Jane Williams", "age": 25, "email": "janewilliams@example.com"},
#            {"name": "Mike Roger",    "age": 35, "email": "mikeroger@example.com"}]
# result = collection.insert_many(data)
# print('Inserted ID', result.inserted_ids)


# data={'name':'raju'}
# result=collection.find(data)
# for i in result:
    # print(i)

    
# data={'name':'raju','age':20}
# result=collection.find(data)
# for i in result:
#     print(i)

# data={'name':'vinay'}
# collection.delete_one(data)
# print('data deleted')


# document_id = ObjectId('65241702893582095644ce5b')
# result = collection.delete_one({"_id": document_id})
# if result.deleted_count == 1:
#             print (f"Document with _id {document_id} deleted successfully.")
# else:
#             print (f"No document found with _id {document_id}.")


# result=collection.find()
# for i in result:
#     print(i)

# filter={'name':'vindu'}
# update={'$set':{'age':20}}
# collection.update_one(filter, update)

# filter={'name':'Mike Roger'}
# update={'$set':{'email':'mile@123'}}
# collection.update_many(filter,update)

db = client['VINAY']
collection = db['vindu_collection']
data={'place':'guntakal'}
result=collection.insert_one(data)
print(result.inserted_id)