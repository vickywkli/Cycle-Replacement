"""
Generate fake but realistic datasets for cycle replacement pipeline.

This replaces raw Excel / CSV inputs from the original notebook.
All data is safe for GitHub and reproducible.
"""

from pathlib import Path
import pandas as pd
import numpy as np
import random

# -------------------------------------------------
# Setup
# -------------------------------------------------
random.seed(42)
np.random.seed(42)

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

N_CONTRACTS = 40
MAX_UNITS_PER_CONTRACT = 4

branches = ["HK", "WK", "EN", "EK"]

# -------------------------------------------------
# 1) Customers
# -------------------------------------------------
customers = []
for i in range(N_CONTRACTS):
    customers.append({
        "CustomerId": 1000 + i,
        "CustomerName": f"FAKE CUSTOMER {i+1}"
    })

df_customers = pd.DataFrame(customers)
df_customers.to_csv(DATA_DIR / "customers.csv", index=False)

# -------------------------------------------------
# 2) Units
# -------------------------------------------------
units = []
unit_counter = 1

for i, cust in enumerate(customers):
    contract_no = f"OM{6000 + i}"
    branch = random.choice(branches)
    n_units = random.randint(2, MAX_UNITS_PER_CONTRACT)

    for _ in range(n_units):
        units.append({
            "UnitNo": f"U{unit_counter:04d}",
            "ContractNo": contract_no,
            "CustomerId": cust["CustomerId"],
            "vBranchID": branch,
            "InstallationYear": random.randint(1985, 2018),
            "ServiceStatusCode": random.choice(["A", "A", "A", "S"])  # mostly active
        })
        unit_counter += 1

df_units = pd.DataFrame(units)
df_units.to_csv(DATA_DIR / "units.csv", index=False)

# -------------------------------------------------
# 3) Safety test dates
# -------------------------------------------------
safety = []
for u in units:
    safety.append({
        "UnitNo": u["UnitNo"],
        "last_safety_test": pd.Timestamp(
            year=random.randint(2022, 2024),
            month=random.randint(1, 12),
            day=random.randint(1, 28)
        ),
        "test_type": random.choice(["yearly", "full load"])
    })

df_safety = pd.DataFrame(safety)
df_safety.to_csv(DATA_DIR / "safety.csv", index=False)

# -------------------------------------------------
# 4) Callbacks (3 years)
# -------------------------------------------------
callbacks = []
for u in units:
    for year in [2023, 2024, 2025]:
        for _ in range(random.randint(1, 6)):
            callbacks.append({
                "UnitNo": u["UnitNo"],
                "CallbackDate": pd.Timestamp(
                    year=year,
                    month=random.randint(1, 12),
                    day=random.randint(1, 28)
                ),
                "Component": random.choice(["Drive", "Door", "Controller"]),
                "DowntimeHours": random.randint(0, 24)
            })

df_callbacks = pd.DataFrame(callbacks)
df_callbacks.to_csv(DATA_DIR / "callbacks.csv", index=False)

print("✅ Dataset generated in ./data/")
