import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw", "simulated-data-raw")
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, "processed", "processed_data.pkl")
CSV_DATA_PATH = os.path.join(DATA_DIR, "processed", "processed_data.csv")
X_TEST_PATH = os.path.join(DATA_DIR, "test", "X_test.pkl")
Y_TEST_PATH = os.path.join(DATA_DIR, "test", "y_test.pkl")

MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "stacked_model.pkl")
