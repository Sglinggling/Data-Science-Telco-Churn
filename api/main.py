from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Chargement du pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/model.pkl')

model = joblib.load(MODEL_PATH)

@app.route('/', methods=['GET'])
def home():
    return "<h1>API Churn Telco : En ligne</h1><p>Utilisez l'endpoint <b>/predict</b> en POST.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df_input = pd.DataFrame(data)
        prediction = model.predict(df_input)
        result = int(prediction[0])
        return jsonify({
            'prediction': result,
            'label': 'Churn (Risque de départ)' if result == 1 else 'No Churn (Fidèle)'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)