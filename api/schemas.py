from pydantic import BaseModel

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