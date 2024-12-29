import pandas as pd

def extract_data(file_path: str):
    # Lisez les données depuis un fichier CSV (peut être modifié pour d'autres sources)
    df = pd.read_csv(file_path)
    print(f"Data extracted from {file_path}")
    return df

# Exemple d'utilisation
# df = extract_data("data.csv")
