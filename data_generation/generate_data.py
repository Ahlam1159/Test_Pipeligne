import pandas as pd
import random

def generate_data(file_path: str, rows: int = 100):
    data = {
        "id": [i for i in range(1, rows + 1)],
        "name": [f"Name_{i}" for i in range(1, rows + 1)],
        "age": [random.randint(18, 60) for _ in range(rows)],
        "city": [random.choice(["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]) for _ in range(rows)],
        "salary": [round(random.uniform(30000, 120000), 2) for _ in range(rows)],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Data generated and saved to {file_path}")

generate_data("data.csv")
