import pandas as pd

from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:root@localhost:5432/retail"
)

files = [
    "products",
    "branches",
    "inventory",
    "sales",
    "shrinkage"
]

for table in files:

    df = pd.read_csv(
        f"data/{table}.csv"
    )

    df.to_sql(
        table,
        engine,
        if_exists="append",
        index=False
    )

print("Data Loaded")