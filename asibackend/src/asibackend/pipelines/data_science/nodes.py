
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout



def scale_data(df: pd.DataFrame) -> pd.DataFrame:
    scaler = StandardScaler()
    columns_to_scale = [ 'EngagementSurvey', 'EmpSatisfaction', 'DaysLateLast30', 'Absences', 'YearsAtCompany']
    df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])

    joblib.dump(scaler, '../../data/04_scalers/scaler.pkl')
    
    return df



def one_hot_encoding(df: pd.DataFrame) -> pd.DataFrame:

    columns_to_one_hot_encoding = ['Department', 'PerformanceScore']

    encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
    encoded_array = encoder.fit_transform(df[columns_to_one_hot_encoding])

    encoded_df = pd.DataFrame(
        encoded_array,
        columns=encoder.get_feature_names_out(columns_to_one_hot_encoding),
        index=df.index
    )

    df = df.drop(columns=columns_to_one_hot_encoding)
    df = pd.concat([df, encoded_df], axis=1)

    joblib.dump(encoder, '../../data/05_encoders/encoder.pkl')
    return df



def split_data(df: pd.DataFrame) -> tuple:
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
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)
    model.save("../../data/03_models/trained_model.keras")

    return model



def evaluate_model(model: Sequential, X_test: pd.DataFrame, y_test: pd.DataFrame):
    loss, mae = model.evaluate(X_test, y_test)
    print(f"Test Loss (MSE): {loss}, Test MAE: {mae}")


