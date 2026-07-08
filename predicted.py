import joblib
import pandas as pd

pipeline=joblib.load("model/pipeline.pkl")

def predict(data:dict):
    df=pd.DataFrame([data])
    prediction=pipeline.predict(df)[0]

    probability=pipeline .predict_proba(df)[0].tolist()

    return{
        "prediction":int(prediction),
        "probability":{
            "no survival":probability[0],
            "survival":probability[1]

        }
    }