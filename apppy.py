from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('artifacts/model.pkl', 'rb'))

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "Hi there, I,m working  with the new API!!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print(data)  # For debugging

        # Convert categorical values to numeric
        gender = 1 if data['Gender'].lower() == 'female' else 0
        married = 1 if data['Married'].lower() == 'married' else 0
        credit_history = 1 if data['Credit_History'].lower() == 'cleard debts' else 0

        # Create features array
        features = pd.DataFrame({
            'Gender': [gender],
            'Married': [married],
            'ApplicantIncome': [data['ApplicantIncome']],
            'LoanAmount': [data['LoanAmount']],
            'Credit_History': [credit_history]
        })

        # Make prediction
        prediction = model.predict(features)

        # Return prediction result
        return jsonify({
            "loan_approve_status": "Approved" if prediction[0] == 1 else "Not Approved"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)