### Création des tables nous aurons 3 tables les entrées, sorties et les features
from sqlalchemy import Column, Integer, Float, String, JSON, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.database import Base

#Creation de la table des données d'entrée de l'employé 

class EmployeeInput(Base):
    __tablename__ = "employee_inputs"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    charge_travail = Column(Integer, nullable=False)
    revenu_mensuel = Column(Integer, nullable=False)
    heure_supplementaires = Column(Integer, nullable=False)
    nombre_participation_pee = Column(Integer, nullable=False)
    annee_experience_totale = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    annes_sous_responsable_actuel = Column(Integer, nullable=False)
    nombre_experiences_precedentes = Column(Integer, nullable=False)
    statut_marital_célibataire = Column(Float, nullable=False)
    distance_domicile_travail = Column(Integer, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    employee_output = relationship(
        "EmployeeOutput",
        back_populates="employee_input",
        uselist=False
    )
    
    
# Création de la tables de la sortie de la prédiction

class EmployeeOutput(Base):
    __tablename__ = "employee_outputs"

    id_output = Column(Integer, primary_key=True, autoincrement=True, index=True)

    employee_id = Column(
        Integer,
        ForeignKey("employee_inputs.id"),
        nullable=False
    )

    a_quitte_l_entreprise = Column(Integer, nullable=False)

    probability = Column(Float, nullable=False)

    model_version = Column(String, nullable=False)

    created_at = Column(
        TIMESTAMP(timezone=True),
        server_default=func.now()
    )

    employee_input = relationship(
        "EmployeeInput",
        back_populates="employee_output"
    )