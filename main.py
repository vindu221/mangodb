from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
# @app.get("/my_first_api")
# async def creat_api():
#      name_1="vinay"
#      surname_1="patnam"
#      name_2="jeethu"
#      surname_2="kakarala"


#      full_name_1=name_1+surname_1
#      full_name_2=name_2+surname_2
#      return{"PERSON_1":full_name_1,"PERSON_2":full_name_2}

#post api using base modul
class Item(BaseModel):
     name:str
     age:int
     salary:float
@app.post("/post_api")
async def creat_new_func(item:Item):
     description=f"{item.name}"+" "+f"{item.age}"+" "+f"{item.salary}"
     return description 

