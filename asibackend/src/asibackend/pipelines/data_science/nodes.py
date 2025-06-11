
import joblib
import pandas as pd
import os
from sklearn.linear_model import LinearRegression
from sklearn.metrics import max_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

def scale_data(df: pd.DataFrame) -> pd.DataFrame:

    powerTransformer = PowerTransformer(method='yeo-johnson')
    salary_reshaped = df['Salary'].values.reshape(-1, 1)
    df['Salary'] = powerTransformer.fit_transform(salary_reshaped)

    minMaxScaler = MinMaxScaler()
    engagementSurveyScaled = df['EngagementSurvey'].values.reshape(-1, 1)
    df['EngagementSurvey'] = minMaxScaler.fit_transform(engagementSurveyScaled)

    standardScaler = StandardScaler()
    columns_to_scale = [ 'EmpSatisfaction', 'DaysLateLast30', 'Absences', 'YearsAtCompany', 'SpecialProjectsCount']
    df[columns_to_scale] = standardScaler.fit_transform(df[columns_to_scale])

    joblib.dump(powerTransformer, '../../data/04_scalers/powerTransformer.pkl')
    joblib.dump(minMaxScaler, '../../data/04_scalers/minMaxScaler.pkl')
    joblib.dump(standardScaler, '../../data/04_scalers/standardScaler.pkl')
    
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

    early_stop = EarlyStopping(monitor='val_loss', patience=50, restore_best_weights=True)

    model = Sequential([
        Dense(100, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.4),
        Dense(50, activation='relu'),
        Dropout(0.4),
        Dense(20, activation='relu'),
        Dropout(0.3),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    history = model.fit(X_train, y_train, epochs=600, batch_size=4, validation_split=0.3, callbacks=[early_stop])
    model.save("../../data/03_models/trained_model.keras")

    # plt.plot(history.history['loss'], label='Train Loss (MSE)')
    # plt.plot(history.history['val_loss'], label='Validation Loss (MSE)')
    # plt.xlabel('Epoch')
    # plt.ylabel('Loss')
    # plt.legend()
    # plt.title('Krzywe uczenia')
    # plt.show()

    return model

def evaluate_model(model: Sequential, X_test: pd.DataFrame, y_test: pd.DataFrame):
    loss, mae = model.evaluate(X_test, y_test)
    print(f"Test Loss (MSE): {loss}, Test MAE: {mae}")


