from fastapi import FastAPI
from pymongo import MongoClient
app=FastAPI()
client=MongoClient("mongodb+srv://vinaypatnam921:Vinay%40123@cluster0.oput5up.mongodb.net/")
db=client["API"]
collection=db["api_operations"]
# @app.post("/post_api")
# async def assignment(item:dict):
#     result=collection.insert_one(item)
#     return "inserted sussefully"

# from fastapi import FastAPI
# app=FastAPI()
# @app.post("/dict_post_api")
# async def create_dict_func(item:dict):
#     data=item["data"]["location"]
#     print(data)



# @app.post("/find_api")
# async def assignment_find(item:dict):
#     result=collection.find_one(item)
#     return result["degree"]

@app.post("/update_api")
async def assignment_update(item:dict):
    result=collection.update_one(item)
    return result

# @app.post("/delete_api")
# async def assignment_delete(item2:dict):
#     result=collection.delete_one(item2)
#     return "delet is susess "
