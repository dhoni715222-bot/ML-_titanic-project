from fastapi import FastAPI

from predicted import predict
from schemas import Passenger

app=FastAPI(
    title="titanic survival API",
    version="1.0"
)

@app.get("/")
def home():

    return{
        "message":"Titanic prediction API is running."
    }

@app.post("/predict")
def predict_survival(passenger:passenger):

    result=predict(passenger.model_dump())
    return result
