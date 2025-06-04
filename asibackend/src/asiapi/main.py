import os
import pandas as pd
import joblib

from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware


model = load_model('../../data/03_models/trained_model.keras')
scaler = joblib.load('../../data/04_scalers/scaler.pkl')
encoder = joblib.load('../../data/05_encoders/encoder.pkl')

columnsToOneHotEncoding = ['Department', 'PerformanceScore']
columnsToScale = [ 'EngagementSurvey', 'EmpSatisfaction', 'DaysLateLast30', 'Absences', 'YearsAtCompany']

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    department: str
    performanceScore: str
    engagmentSurvey: float
    empSatisfaction: float
    daysLateLast30: float
    absences: float
    yearsAtCompany: float

@app.post("/predict")
def predict(data: InputData):

    print(data)

    input_dict = {
        'Department': [data.department],
        'PerformanceScore': [data.performanceScore],
        'EngagementSurvey': [data.engagmentSurvey],
        'EmpSatisfaction': [data.empSatisfaction],
        'DaysLateLast30': [data.daysLateLast30],
        'Absences': [data.absences],
        'YearsAtCompany': [data.yearsAtCompany]
    }

    df = pd.DataFrame(input_dict)

    encoded_array = encoder.transform(df[columnsToOneHotEncoding])
    encoded_df = pd.DataFrame(
        encoded_array,
        columns=encoder.get_feature_names_out(columnsToOneHotEncoding),
        index=df.index
    )
    
    df = df.drop(columns=columnsToOneHotEncoding)
    df = pd.concat([df, encoded_df], axis=1)

    df[columnsToScale] = scaler.transform(df[columnsToScale])

    prediction = model.predict(df)

    return str(prediction[0][0])
