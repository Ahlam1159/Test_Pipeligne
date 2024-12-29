import pandas as pd

def transform_data(input_file: str, output_file: str):
    df = pd.read_csv(input_file)

    # Filtrer les données où l'âge est inférieur à 25
    df = df[df["age"] >= 25]

    # Calculer la taxe (10% du salaire)
    df["tax"] = df["salary"] * 0.10

    # Sauvegarder les données transformées dans un nouveau fichier CSV
    df.to_csv(output_file, index=False)
    print(f"Transformed data saved to {output_file}")

# Exemple d'utilisation
# transform_data("data.csv", "transformed_data.csv")
