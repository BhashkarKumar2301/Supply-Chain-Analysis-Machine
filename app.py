from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("supply_chain_revenue_predictor.pkl")

@app.route('/')
def index():
    return "Supply Chain Revenue Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]
    return jsonify({'predicted_revenue': round(prediction, 2)})

if __name__ == '__main__':
    app.run()
