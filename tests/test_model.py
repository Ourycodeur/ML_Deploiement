from pathlib import Path


import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "Modèle" / "logistic_model.pkl"

model = joblib.load(model_path)

## Testons les prédictions 

def test_model_prediction():

    data = pd.DataFrame([{
        "charge_travail": 3,
        "revenu_mensuel": 4000,
        "heure_supplementaires": 5,
        "nombre_participation_pee": 1,
        "annee_experience_totale": 10,
        "age": 35,
        "annes_sous_responsable_actuel": 4,
        "nombre_experiences_precedentes": 2,
        "statut_marital_célibataire": 1,
        "distance_domicile_travail": 15
    }])

    prediction = model.predict(data)[0]

    assert prediction in [0, 1]
    
    
    
# Test des performances 

