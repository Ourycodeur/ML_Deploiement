# Importation des bibliothèques nécessaires
import joblib
<<<<<<< HEAD
import pandas as pd
import numpy as np
from fastapi import FastAPI, Depends
import uvicorn
from api.database import SessionLocal, engine
from api.crud import create_employee_input, creation_prediction
from api.schemas import EmployeeData
from sqlalchemy.orm import Session
from db.models import Base

## Création de la base de données et des tables
Base.metadata.create_all(bind=engine)

# Chargement du modèle et des features
model = joblib.load("C:\\Users\\El. OURY BALDE\\Downloads\\P4\\P4\\Modèle\\logistic_model.pkl")

# Création de l'application FastAPI
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
   
## Endpoint pour les prédictions     

# Définition du modèle de données pour les prédictions


@app.get("/")
def read_root():
    return {"message" :"Bienvenue dans l'API de prédiction de départ ou de retention d'un employé"}

"""
@app.get("/predict/info")
def predict_info():
    return {
        "description": "Cet endpoint permet de prédire si un employé va quitter l'entreprise.",
        "fonctionnement": [
            "Les données sont reçues via une requête POST",
            "Le modèle de machine learning analyse les features",
            "Une prédiction est générée (0 = reste, 1 = quitte)",
            "Une probabilité est calculée",
            "Les résultats sont enregistrés dans PostgreSQL"
        ],
        "Entré": "Données RH de l’employé",
        "Sortie": {
            "predicted_label": "0 ou 1",
            "probability": "valeur entre 0 et 1"
        }
    }
    
"""

# Endpoint pour les prédictions
@app.post(
    "/predict",
    summary= "Prédiction de départ d'un départ d'un employé ",
    description= """
    Cet endpoint permet de prédire si un employé va quitter l’entreprise.

    Fonctionnement :
    - Les données sont envoyées au modèle ML
    - Le modèle retourne une prédiction (0 ou 1) (0 => rester et 1 => quitter)
    - Une probabilité est calculée pour connaître la probabilité de départ et un message est rétourné suite à la probabilité
    - Les résultats sont enregistrés en base de données et celle que nous utilisons est Postgresql
    - Entré: Données RH de l’employé,
    - Sortie :
            predicted_label: 0 ou 1,
            probability": valeur entre 0 et 1
    """,)

def predict(employee_data: EmployeeData, db: Session = Depends(get_db)):
    input_dict = employee_data.model_dump()
    input_df = pd.DataFrame([input_dict])
    
    
    
    #input_df = pd.DataFrame([input_dict])
    
    # Prediction de la probabilité de départ de l'employé
    
    #prediction_proba = model.predict_proba(input_df)[:, 1][0]  # Probabilité de départ
    probability = model.predict_proba(input_df)[:, 1][0]
    predicted_label = model.predict(input_df)[0]  # Prédiction binaire (0 ou 1)
    
    # Conversion 
    
    predicted_label = int(predicted_label)  # Convertir en int pour une meilleure lisibilité
    probability = float(probability)
    
    
    # Sauvegarde des entrées de l'employé dans la base de données
    employee_input  = create_employee_input(
        db=db,
        data=employee_data
    )
    
    
    # Insertion et prediction
    
    creation_prediction(
        db=db,
        employee_input=employee_input,
        a_quitte_l_entreprise=predicted_label,
        probability=probability
    )
    
    predicted_label = int(predicted_label)  # Convertir en int pour une meilleure lisibilité
    probability = float(probability)  # Convertir en float pour une meilleure lisibilité
    
      # Message de prédiction
    message = (
        "L'employé risque de quitter l'entreprise"
        if predicted_label == 1
        else "L'employé risque de rester dans l'entreprise"
    )
    
        
    # Retour de la prédiction et de la probabilité
    return {
        "predicted_label": predicted_label,  # Convertir en int pour une meilleure lisibilité
        "probability": probability,  # Convertir en float pour une meilleure lisibilité
        "message": message  # Message de prédiction
    }
    


@app.get("/health")
def health():
    return {"status": "ok"}


# Lancement de l'application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



