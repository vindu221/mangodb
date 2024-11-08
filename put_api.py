from fastapi import FastAPI

app = FastAPI()

dic={1:"SAYANTAN", 2:"VINAY", 3:"JEEVIKA", 4:"ANIL"}

print("ORIGINAL DICTIONARY:",dic)

@app.put("/update_api/{item_id}")
def update_item(item_id: int, new_item: dict): 
    original_value=dic[item_id]    
    print("ORIGINAL VALUE:",original_value)    
    new_value=new_item["new_value"]
    print("NEW VALUE:",new_value)
    dic[item_id]=new_value    
    print("NEW DICTIONARY:",dic)    
    return f"Value Updated Successfully for Key - {item_id}."