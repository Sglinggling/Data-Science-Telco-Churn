import requests

url = 'http://127.0.0.1:5000/predict'

# On crée une liste avec les données d'un client fictif
data = [{
    "gender": "Female",
    "SeniorCitizen": 0,
    "Partner": "No",
    "Dependents": "No",
    "tenure": 1, 
    "PhoneService": "No",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "No",
    "OnlineBackup": "No",
    "DeviceProtection": "No",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "Month-to-month",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 29.85,
    "TotalCharges": 29.85
}]

print("Envoi des données au modèle...")

try:
    # Envoie la requête POST avec le JSON
    response = requests.post(url, json=data)
    
    # On affiche la réponse
    print("Statut de la requête :", response.status_code)
    print("Réponse du modèle :", response.json())

except Exception as e:
    print("Erreur lors du test :", e)