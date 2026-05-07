from db.models import EmployeeInput, EmployeeOutput


## Insertions des features d'entrée de l'employé dans la base de données

def create_employee_input(db,data):
    employee = EmployeeInput(
        charge_travail=data.charge_travail,
        revenu_mensuel=data.revenu_mensuel,
        heure_supplementaires=data.heure_supplementaires,
        nombre_participation_pee=data.nombre_participation_pee,
        annee_experience_totale=data.annee_experience_totale,
        age=data.age,
        annes_sous_responsable_actuel=data.annes_sous_responsable_actuel,
        nombre_experiences_precedentes=data.nombre_experiences_precedentes,
        statut_marital_célibataire=data.statut_marital_célibataire,
        distance_domicile_travail=data.distance_domicile_travail
    )
    
    db.add(employee)
    db.commit()
    db.refresh(employee)
    
    return employee

## Insertions des résultats de prédiction dans la base de données

def creation_prediction(
    db,
    employee_input,
    a_quitte_l_entreprise,
    probability
):
    prediction = EmployeeOutput(
        employee_id=employee_input.id,
        a_quitte_l_entreprise=a_quitte_l_entreprise,
        probability=probability,
        model_version="1.0"  # Vous pouvez ajuster la version du modèle selon vos besoins
    )
    
    db.add(prediction)
    db.commit()
    db.refresh(prediction)
    
    return prediction
    
    
    