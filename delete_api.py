from fastapi import FastAPI
app=FastAPI
dict_name={
    1: {"name": "Sayantan", "age": 35},
    2: {"name": "Vinay", "age": 20},
    3: {"name": "Jeevika", "age": 21}
}
print(f"DICTIONARY BEFORE DELETING: {dict_name}")
@app.delete("/delete_api/{item_id}")
async def delete_fun(item_id:int): 
    if item_id in dict_name:
        del dict_name[item_id]
        print(f"DICTIONARY after DELETING: {dict_name}") 
        return "deleted"
    else:
        print("i can not find item") 
        return "i can not find item"    

