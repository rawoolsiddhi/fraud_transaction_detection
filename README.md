# 🕵️ Fraud Transaction Detection

This is an end-to-end machine learning project to detect fraudulent financial transactions using a stacking ensemble model (Random Forest + XGBoost). It includes preprocessing, modeling, evaluation, prediction, and a user-friendly Streamlit web app.



## 🚀 Features

- EDA + Feature Engineering on synthetic fraud transaction dataset
- Stacked Ensemble Classifier (Random Forest + XGBoost + Logistic Regression)
- Hyperparameter tuning with cross-validation
- Pickle and CSV support for predictions
- Logging of all predictions to `logs/`
- Web-based fraud detection via Streamlit interface



## 🧠 Algorithms Used

- **Random Forest**
- **XGBoost**
- **Logistic Regression**
- Combined using `StackingClassifier` from scikit-learn

---



---

## 🧪 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/rawoolsiddhi/fraud_transaction_detection.git
cd fraud_transaction_detection

```

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate    # for Windows
# or
source venv/bin/activate # for Linux/macOS

3. Install Requirements

pip install -r requirements.txt

4. Run the App

streamlit run app.py



## Upload Format (CSV/PKL)
Uploaded file must include the following columns:

TRANSACTION_ID, TX_DATETIME, CUSTOMER_ID, TERMINAL_ID, TX_AMOUNT, TX_TIME_SECONDS, TX_TIME_DAYS


📦 Model
The model is trained on a large-scale simulated fraud dataset with balanced class handling and saved as models/stacked_model.pkl.

📃 License
MIT License


Made  by Siddhi Rawool

Feel free to connect on LinkedIn
https://www.linkedin.com/in/siddhi-rawool-783059248/
