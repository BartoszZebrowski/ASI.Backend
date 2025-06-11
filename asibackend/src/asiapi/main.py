import os
import pandas as pd
import joblib

from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware


model = load_model('../../data/03_models/trained_model.keras')

standardScaler = joblib.load('../../data/04_scalers/standardScaler.pkl')
minMaxScaler = joblib.load('../../data/04_scalers/minMaxScaler.pkl')
powerTransformer = joblib.load('../../data/04_scalers/powerTransformer.pkl')

encoder = joblib.load('../../data/05_encoders/encoder.pkl')

columnsToOneHotEncoding = ['Department', 'PerformanceScore']
columnsToStandardScaler = ['EmpSatisfaction', 'DaysLateLast30', 'Absences', 'YearsAtCompany', 'SpecialProjectsCount']
columnsToPowerTransformer = ['Salary']
columnsToMinMaxScaler = [ 'EngagementSurvey']


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
    specialProjectsCount: float

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
        'YearsAtCompany': [data.yearsAtCompany],
        'SpecialProjectsCount': [data.specialProjectsCount]
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

    df[columnsToStandardScaler] = standardScaler.transform(df[columnsToStandardScaler])
    df[columnsToMinMaxScaler] = minMaxScaler.transform(df[columnsToMinMaxScaler])

    prediction = model.predict(df)

    salary = powerTransformer.inverse_transform([[prediction[0][0]]])[0][0]

    return int(salary)
