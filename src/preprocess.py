import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def apply_feature_engineering(df):
    df["TX_DATETIME"] = pd.to_datetime(df["TX_DATETIME"])
    df["TX_HOUR"] = df["TX_DATETIME"].dt.hour
    df["TX_DAY_OF_WEEK"] = df["TX_DATETIME"].dt.dayofweek
    df["TX_WEEK_OF_YEAR"] = df["TX_DATETIME"].dt.isocalendar().week
    df["TX_IS_WEEKEND"] = df["TX_DAY_OF_WEEK"].apply(lambda x: 1 if x >= 5 else 0)
    df.drop(columns=["TX_DATETIME"], inplace=True)
    
    df["TX_TIME_SECONDS"] = pd.to_numeric(df["TX_TIME_SECONDS"], errors="coerce")
    df["TX_TIME_DAYS"] = pd.to_numeric(df["TX_TIME_DAYS"], errors="coerce")

    df.fillna(0, inplace=True)

    le_customer = LabelEncoder()
    le_terminal = LabelEncoder()
    df["CUSTOMER_ID"] = le_customer.fit_transform(df["CUSTOMER_ID"])
    df["TERMINAL_ID"] = le_terminal.fit_transform(df["TERMINAL_ID"])

    scaler = StandardScaler()
    df["TX_AMOUNT"] = scaler.fit_transform(df[["TX_AMOUNT"]])

    return df
