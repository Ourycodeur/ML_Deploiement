import time
from fastapi import Path
import pandas as pd
import joblib
from pathlib import Path


# Charger le modèle
BASE_DIR = Path(__file__).resolve().parent.parent

model_path = BASE_DIR / "Modèle" / "logistic_model.pkl"

model = joblib.load(model_path)

def test_prediction_speed():

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

    start = time.time()

    model.predict(data)

    end = time.time()

    assert (end - start) < 1