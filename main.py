from flask import Flask, request, jsonify
from joblib import load
import pandas as pd


app = Flask(__name__)

# Load the trained model and scaler
model = load('model.joblib')
scaler = load('scaler.joblib')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract JSON data from the request
        data = request.get_json(force=True)
        # Convert data into DataFrame
        df = pd.DataFrame([data])
        # Scale the input data
        scaled_data = scaler.transform(df)
        # Predict
        prediction = model.predict(scaled_data)
        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)


# This is the Flask application for predicting something based on the trained model.
