import pandas as pd

def validate_data(file_path: str):
    df = pd.read_csv(file_path)

    # Validation des données
    validations = {
        "no_missing_values": df.isnull().sum().sum() == 0,
        "age_range_valid": df["age"].between(18, 60).all(),
        "salary_positive": (df["salary"] > 0).all(),
        "unique_ids": df["id"].is_unique,
    }

    for check, result in validations.items():
        if result:
            print(f"Validation passed: {check}")
        else:
            print(f"Validation failed: {check}")
            raise ValueError(f"Validation failed: {check}")

    print("All validations passed!")

# Exemple d'utilisation
# validate_data("data.csv")
