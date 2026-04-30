import pandas as pd
import numpy as np

import os
print(os.listdir())
print(os.listdir("dataset"))

# STEP 1 – load dataset FIRST
df = pd.read_csv("dataset/heart_cleveland_upload.csv")

# STEP 2 – check columns (debug)
print(df.columns)

# STEP 3 – clean data
df.replace("?", np.nan, inplace=True)
df = df.apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

# STEP 4 – FIX target column (for your dataset)
df["condition"] = df["condition"].apply(lambda x: 1 if x > 0 else 0)

# STEP 5 – save cleaned file
df.to_csv("dataset/heart_cleaned.csv", index=False)

print("Cleaned dataset ready!")