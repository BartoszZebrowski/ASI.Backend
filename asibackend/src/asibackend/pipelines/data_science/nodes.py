
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

def scale_data(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    columnsToScale = [ 'EngagementSurvey', 'EmpSatisfaction', 'DaysLateLast30', 'Absences', 'YearsAtCompany']
    df[columnsToScale] = scaler.fit_transform(df[columnsToScale])
    
    return df, scaler


     
def one_hot_encoding(df: pd.DataFrame) -> pd.DataFrame:
    columnsToOneHotEncoding = ['Position', 'Department', 'PerformanceScore']

    encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    encoder.fit(df[columnsToOneHotEncoding])
    
    return df, encoder


def split_data(df: pd.DataFrame,) -> tuple:
    X = df.drop(columns=['Salary'])
    y = df['Salary']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test


def train_model(X_train: pd.DataFrame, y_train: pd.DataFrame) -> LinearRegression:

    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.3),
        Dense(32, activation='relu'),
        Dropout(0.3),
        Dense(24, activation='relu'),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(X_train, y_train, epochs=1000, batch_size=32, validation_split=0.2)

    return model

    # regressor = LinearRegression()
    # regressor.fit(X_train, y_train)
    # return regressor


def evaluate_model(model: Sequential, X_test: pd.DataFrame, y_test: pd.DataFrame):

    loss, mae = model.evaluate(X_test, y_test)
    print(f"Test Loss (MSE): {loss}, Test MAE: {mae}")


    # regressor: LinearRegression, X_test: pd.DataFrame, y_test: pd.Series) -> dict[str, float]:
    # y_pred = regressor.predict(X_test)
    # score = r2_score(y_test, y_pred)
    # mae = mean_absolute_error(y_test, y_pred)
    # me = max_error(y_test, y_pred)
    # logger = logging.getLogger(__name__)
    # logger.info("Model has a coefficient R^2 of %.3f on test data.", score)
    # return {"r2_score": score, "mae": mae, "max_error": me}


