from api.crud import create_employee_input


def test_create_employee_input(db_session):

    class FakeData:
        charge_travail = 3
        revenu_mensuel = 4000
        heure_supplementaires = 5
        nombre_participation_pee = 1
        annee_experience_totale = 10
        age = 35
        annes_sous_responsable_actuel = 4
        nombre_experiences_precedentes = 2
        statut_marital_célibataire = 1
        distance_domicile_travail = 15

    employee = create_employee_input(
        db=db_session,
        data=FakeData()
    )

    assert employee.id is not None

    assert employee.age == 35
    
    
from api.database import get_db

def test_get_db():
    db_gen = get_db()
    db = next(db_gen)
    
    assert db is not None
    
    db.close()
    
def test_db_integration(db_session):

    assert db_session is not None