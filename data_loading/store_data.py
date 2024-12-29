import sqlite3
import pandas as pd

def store_data(input_file: str, db_file: str, table_name: str):
    df = pd.read_csv(input_file)

    # Connexion à la base de données SQLite
    conn = sqlite3.connect(db_file)

    # Sauvegarder les données dans la table
    df.to_sql(table_name, conn, if_exists="replace", index=False)

    # Fermer la connexion
    conn.close()
    print(f"Data stored in {table_name} table of {db_file}")

# Exemple d'utilisation
# store_data("transformed_data.csv", "dataops_pipeline.db", "transformed_data")
