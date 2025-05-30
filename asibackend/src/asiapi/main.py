from fastapi import FastAPI
from pydantic import BaseModel
from kedro.framework.context import KedroContext
from kedro.framework.hooks import _create_hook_manager
from kedro.framework.startup import bootstrap_project

import os

project_path = os.getcwd()
metadata = bootstrap_project(project_path)
hook_manager = _create_hook_manager()
context = KedroContext(metadata.package_name, project_path, hook_manager)

catalog = context.catalog
model = catalog.load("model")

app = FastAPI()

class InputData(BaseModel):
    # Position: str ## dropdown z mozliwoscami wyboru: 
    
    #     ## Accountant I
    #     ## Accountant I
    #     ## Accountant I
    #     ## Accountant I
    #     ## Accountant I
    #     ## Accountant I
    #     ## Administrative Assistant
    #     ## Area Sales Manager
    #     ## BI Developer
    Department: str
        ## Admin Offices
        ## Executive Office
        ## IT/IS
        ## Production
        ## Sales
        ## Software Engineering
    PerformanceScore: str
        ## Exceeds
        ## Fully Meets
        ## Needs Improvement
        ## PIP
    EngagmentSurvey: float ##od zera do 5 z czescia po przecinku
    EmpSatisfaction: float ##od zera do 5
    DaysLateLast30: float
    Absences: float
    YearsAtCompany: float 





@app.post("/predict/")
def predict(data: InputData):
    features = data.dict()
    # Użyj modelu bez pipeline
    import numpy as np
    input_array = np.array([[features["feature1"], features["feature2"], features["feature3"]]])
    prediction = model.predict(input_array)
    return {"prediction": prediction.tolist()}
