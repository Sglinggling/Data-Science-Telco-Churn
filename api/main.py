from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# 1. Chargement du Pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../models/model.pkl')

model = joblib.load(MODEL_PATH)

# Page d'accueil
@app.route('/', methods=['GET'])
def home():
    return "<h1>API Churn Telco : En ligne </h1><p>Utilisez l'endpoint <b>/predict</b> en POST pour obtenir une prédiction.</p>"

# Route pour la prédiction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Réception des données au format JSON
        data = request.get_json()
        
        # Transformation en DataFrame pour que la Pipeline puisse traiter les données
        df_input = pd.DataFrame(data)
        
        # Prédiction
        prediction = model.predict(df_input)
        
        # Réponse
        result = int(prediction[0])
        return jsonify({
            'prediction': result,
            'label': 'Churn (Risque de départ)' if result == 1 else 'No Churn (Fidèle)'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
