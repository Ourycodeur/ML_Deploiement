from fastapi.testclient import TestClient
from api.main import app

## Definissons la variable client 

client = TestClient(app)

def test_root():
    reponse = client.get("/")
    
    assert reponse.status_code == 200
    
    assert reponse.json() == {
        "message" :"Bienvenue dans l'API de prédiction de départ ou de retention d'un employé" 
    }
    
    
# testons les endpoints de prediction 

def test_prediction():

    Entré = {
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
    }

    response = client.post(
        "/predict",
        json=Entré
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_label" in data

    assert "probability" in data

    assert isinstance(data["predicted_label"], int)

    assert isinstance(data["probability"], float)
    
    
# Testons les cas d'erreurs 

def test_prediction_invalid_data():

    Entré = {
        "charge_travail": "erreur",
        "revenu_mensuel": 4000
    }

    response = client.post(
        "/predict",
        json=Entré
    )

    assert response.status_code == 422
    
    
# Testons la santé 

def test_health():
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}