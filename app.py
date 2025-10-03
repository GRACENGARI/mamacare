from flask import Flask, request, jsonify, render_template_string
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

app = Flask(__name__)

# HTML template for the web interface
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Maternal Health Risk Prediction</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
            color: #34495e;
        }
        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
        }
        .high-risk {
            background-color: #e74c3c;
            color: white;
        }
        .mid-risk {
            background-color: #f39c12;
            color: white;
        }
        .low-risk {
            background-color: #27ae60;
            color: white;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🏥 Maternal Health Risk Prediction</h1>
        <form id="predictionForm">
            <div class="form-group">
                <label>Age:</label>
                <input type="number" id="age" required min="10" max="100">
            </div>
            <div class="form-group">
                <label>Systolic BP:</label>
                <input type="number" id="systolicBP" required step="0.01">
            </div>
            <div class="form-group">
                <label>Diastolic BP:</label>
                <input type="number" id="diastolicBP" required step="0.01">
            </div>
            <div class="form-group">
                <label>Blood Sugar (BS):</label>
                <input type="number" id="bs" required step="0.01">
            </div>
            <div class="form-group">
                <label>Body Temperature:</label>
                <input type="number" id="bodyTemp" required step="0.01">
            </div>
            <div class="form-group">
                <label>Heart Rate:</label>
                <input type="number" id="heartRate" required>
            </div>
            <button type="submit">Predict Risk Level</button>
        </form>
        <div id="result"></div>
    </div>

    <script>
        document.getElementById('predictionForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const data = {
                Age: parseFloat(document.getElementById('age').value),
                SystolicBP: parseFloat(document.getElementById('systolicBP').value),
                DiastolicBP: parseFloat(document.getElementById('diastolicBP').value),
                BS: parseFloat(document.getElementById('bs').value),
                BodyTemp: parseFloat(document.getElementById('bodyTemp').value),
                HeartRate: parseInt(document.getElementById('heartRate').value)
            };

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();
                const resultDiv = document.getElementById('result');
                
                if (result.error) {
                    resultDiv.innerHTML = `<div class="result" style="background-color: #e74c3c; color: white;">${result.error}</div>`;
                } else {
                    let className = 'low-risk';
                    if (result.risk_level === 'high risk') className = 'high-risk';
                    else if (result.risk_level === 'mid risk') className = 'mid-risk';
                    
                    resultDiv.innerHTML = `<div class="result ${className}">Risk Level: ${result.risk_level.toUpperCase()}</div>`;
                }
            } catch (error) {
                document.getElementById('result').innerHTML = `<div class="result high-risk">Error: ${error.message}</div>`;
            }
        });
    </script>
</body>
</html>
'''

# Train and save the model
def train_model():
    # Load the data
    df = pd.read_csv('C:/Users/USER/Desktop/ELEVEN LABS/maternal health.csv')
    
    # Prepare features and target
    X = df.drop('RiskLevel', axis=1)
    y = df['RiskLevel']
    
    # Encode target variable
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Save model and encoder
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('encoder.pkl', 'wb') as f:
        pickle.dump(le, f)
    
    print(f"Model trained with accuracy: {model.score(X_test, y_test):.2f}")
    return model, le

# Load model
if os.path.exists('model.pkl') and os.path.exists('encoder.pkl'):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
else:
    model, label_encoder = train_model()

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        # Extract features in the correct order
        features = [[
            data['Age'],
            data['SystolicBP'],
            data['DiastolicBP'],
            data['BS'],
            data['BodyTemp'],
            data['HeartRate']
        ]]
        
        # Make prediction
        prediction = model.predict(features)
        risk_level = label_encoder.inverse_transform(prediction)[0]
        
        return jsonify({
            'risk_level': risk_level,
            'input_data': data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)