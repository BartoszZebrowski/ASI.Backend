import pandas as pd

"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.19.13
"""


def drop_columns(df: pd.DataFrame) -> pd.DataFrame:
    # np.
    return df.drop(columns=["do_usuniecia"])