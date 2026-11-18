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