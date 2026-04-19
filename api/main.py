# Importation des bibliothèques nécessaires
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

# Chargement du modèle et des features
model = joblib.load("../Modèle/logistic_model.pkl")
features = joblib.load("../Modèle/features.pkl")
#explainer = shap.Explainer(model, features)

# Création de l'application FastAPI
app = FastAPI()
# Définition du modèle de données pour les prédictions
class EmployeeData(BaseModel):
    charge_travail: int
    revenu_mensuel: int
    heure_supplementaires: int
    nombre_participation_pee: int
    annee_experience_totale: int
    age: int
    annes_sous_responsable_actuel: int
    nombre_experiences_precedentes: int
    statut_marital_célibataire: float
    distance_domicile_travail: int

@app.get("/")
def read_root():
    return {"message": "Bienvenue dans l'API de prédiction"}

# Endpoint pour les prédictions
@app.post("/predict")
def predict(data: EmployeeData):

    input_data = np.array([[
        data.charge_travail,
        data.revenu_mensuel,
        data.heure_supplementaires,
        data.nombre_participation_pee,
        data.annee_experience_totale,
        data.age,
        data.annes_sous_responsable_actuel,
        data.nombre_experiences_precedentes,
        data.statut_marital_célibataire,
        data.distance_domicile_travail
    ]])

    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        interpretation = "L'employé risque de quitter"
    else:
        interpretation = "L'employé va rester"

    return {
        "prediction": int(prediction),
        "probabilité_de_quitter": float(proba),
        "interpretation": interpretation
    }

@app.get("/health")
def health():
    return {"status": "ok"}


# Lancement de l'application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



