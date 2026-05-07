import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:root@localhost:5432/ml_project")

try:
	df = pd.read_csv("C:\\Users\\El. OURY BALDE\\Downloads\\P4\\P4\\Dataset\\data.csv")
	df.to_sql("dataset", engine, if_exists="append", index=False)
	print("Dataset inséré avec succès.")
except FileNotFoundError:
	print("Erreur : Le fichier CSV 'C:\\Users\\El. OURY BALDE\\Downloads\\P4\\P4\\Dataset\\data.csv' n'a pas été trouvé. Vérifiez le chemin.")
except Exception as e:
	print(f"Erreur lors de l'insertion : {e}")