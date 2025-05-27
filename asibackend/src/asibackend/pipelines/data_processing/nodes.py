import pandas as pd

"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.13
"""


def drop_columns(df: pd.DataFrame) -> pd.DataFrame:

    df = df.drop(columns=[
        "Employee_Name",
        "EmpID",
        "MarriedID",
        "PositionID",
        "MaritalStatusID",
        "LastPerformanceReview_Date",
        "RecruitmentSource",
        "ManagerName",
        "DateofTermination",
        "RaceDesc",
        "CitizenDesc",
        "MaritalDesc",
        "HispanicLatino",
        "Sex",
        "DOB",
        "Zip",
        "State",
        "Termd",
        "FromDiversityJobFairID",
        "PerfScoreID",
        "EmpStatusID",
        "GenderID",
        "DeptID",
        "ManagerID",
        "SpecialProjectsCount"
    ], 
    errors="ignore")

    return df


def create_train_data(df: pd.DataFrame) -> pd.DataFrame:
    print("dupa")