# src/utils.py
import os
import csv
from datetime import datetime

LOG_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'logs')
LOG_FILE = os.path.join(LOG_DIR, 'predictions_log.csv')

def log_predictions(df):
    os.makedirs(LOG_DIR, exist_ok=True)

    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        # Write header if file didn't exist before
        if not file_exists:
            writer.writerow(['timestamp', 'transaction_id', 'predicted_fraud'])
        for _, row in df.iterrows():
            writer.writerow([datetime.now().isoformat(), row['TRANSACTION_ID'], row['Predicted_Fraud']])
