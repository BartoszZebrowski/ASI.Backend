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
        "SpecialProjectsCount",
        "EmploymentStatus",
        "TermReason",
        "Position"
    ], errors="ignore")

    return df



def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    df['DateofHire'] = pd.to_datetime(df['DateofHire'], format='%m/%d/%Y', errors='coerce')

    df['YearsAtCompany'] = (pd.Timestamp.now() - df['DateofHire']).dt.days / 365.25
    df['YearsAtCompany'] = df['YearsAtCompany'].round().astype(int)

    df = df.drop(columns=['DateofHire'])

    return df