# Deploiement Projet ML en utilisant Git/Github

Deploiement Projet . 

## Getting started

Vous êtes freelance spécialisé en machine learning et vous venez de recevoir une demande de la part de votre client Futurisys, une entreprise innovante qui souhaite rendre ses modèles de machine learning opérationnels et accessibles via une API performante. Vous êtes chargé de déployer un modèle de machine learning en production.

 

-Le directeur technique de Futurisys, Aurélien, vous formule une demande impliquant de : 

-créer une API avec FastAPI (ou équivalent) pour exposer le modèle ;

- écrire des tests unitaires avec Pytest pour garantir sa fiabilité ; 

- et gérer la version du code avec Git pour une collaboration fluide.

 

L'objectif ? Rendre le modèle utilisable en production tout en respectant les meilleures pratiques de l'ingénierie logicielle. À la fin du projet, vous aurez un Proof of Concept (POC) fonctionnel dont vous pourrez être fier !



### Pré-requis

Pour executer en local le projet de deploiement du model de machine learning, vous devez au préalable installer les dépendances nécessaires vous pouvez le faire en une seule commande :

```
pip install -r requirements.txt

```

### Structure du projet

La structure est la suivante :

```
api/
 ├── main.py              # FastAPI app and endpoints
 ├── database.py          # DB connection (SQLAlchemy)
 ├── crud.py              # DB operations
 ├── schemas.py          # Pydantic models
db/
 ├── models.py            # Database tables (SQLAlchemy)
Modèle/
 ├── logistic_model.pkl   # Trained ML model
```





## Executer les tests unitaires et fonctionnels 

```
test
|---conftest.py              # Test de la base de donnée
|---test_api.py		     # Test de chaque endpoint de l'api
|---test_crud.py	     # Test des données d'insertion
|---test_model.py            # Test du model dans sa prediction soit 0 ou 1
|---test_performance.py      # Test de rapidité de prédiction
```

```
on lance directement : pytest
si vous voulez voir de manière détaillé l'affichage de vos test : pytest --cov
```


## Pipeline Machine learning

Etape 1: Recevoir EmployeeData
Etape 2: Convertir en Dataframe
Etape 3: lecture du model à travers joblib
Etape 4: Prédiction de classe 0 ou 1
Etape 5: Enregistrement des inputs et outputs dans la base de donnée

```
Exemple :
def predict(employee_data: EmployeeData, db: Session = Depends(get_db)):
    input_dict = employee_data.model_dump()
    input_df = pd.DataFrame([input_dict])
    
    
    
    input_dict = employee_data.dict() => deprécié donc on utilise dump au lieu de dict
    
     Prediction de la probabilité de départ de l'employé
    
    #prediction_proba = model.predict_proba(input_df)[:, 1][0]  

    # Probabilité de départ
    probability = model.predict_proba(input_df)[:, 1][0]
    predicted_label = model.predict(input_df)[0]  # Prédiction binaire (0 ou 1)
```

## Technologies Utilisées:

* Python 3
* FastApi
* Uvicorn
* Pandas & Numpy
* Scikit-learn (model)
* SQLAlchemy(ORM)
* PostgreSQL (Base de donnée)
* Gradio interface hugging face space
* Jupyter Notebook

## Api :
* / root endpoint : retourne un message de bienvenue
* / prediction : Post/Predict 
	insertion de nos valeurs avec les champs disponibles
	après insertion on exécute et ça nous renvoie :
		Predicted_label = 0 ou 1
		probability de quitter si = 1 message départ else reste
		message (interpretation)

	{
	  "charge_travail": ,
	  "revenu_mensuel": ,
	  "heure_supplementaires":,
	  "nombre_participation_pee":,
	  "annee_experience_totale": ,
	  "age":,
	  "annes_sous_responsable_actuel":,
	  "nombre_experiences_precedentes":,
	  "statut_marital_célibataire": ,
	  "distance_domicile_travail":
	}

	{
  "predicted_label":,
  "probability":,
  "message": ""
}

* /health retourne le status de l'api

* Lancement du projet :
Dan la racine du projet on tape :

uvicorn api.main:app --reload

Chemin d'accès :

http://127.0.0.1:8000

Swagger docs:
http://127.0.0.1:8000/docs

## Deploiement :
Le projet est déployé sur mon espace hugging face space et c'est le suivant :
https://huggingface.co/spaces/MOB2408/Deploy






## Auteurs

* **Mamadou Oury Baldé Data Scientist Machine Learning**
* Ce projet a été réalisé à la suite d'un projet pour le machine learning deploiement avec fastapi + Postgresql
