from fastapi import FastAPI
from pydantic import BaseModel
import joblib
app= FastAPI()
model= joblib.load("model.pkl")
class Flowerdata(BaseModel):
    sepal_length:float
    sepal_width:float
    petal_length:float
    petal_width:float

@app.get("/")
def home():   
    return {"message":"model is running"}

# vicorn main:app --reload 
@app.post("/predict")
def predict(data:Flowerdata):
    input_data=[[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]
    prediction = model.predict(input_data)
    flower_Names = ["setosa","versicolor","virginica"]

    result= flower_Names[int(prediction[0])]
    return {"prediction":result}


@app.get("/bio")
def home():   
    return {"name":"Rohit gurung",
            "age":"20",
            "education":"Graduate"}

class BioData(BaseModel):
    name:str
    age:int
    education:str

@app.post("/biodata")
def data(data:BioData):
    return {"name":data.name,"age":data.age,"education":data.education}
