import pandas as pd

# Load the dataset
df = pd.read_csv("data/candidates_raw.csv")

# Check for missing values
print("\nMISSING VALUES PER COLUMN:")
print("--------------------------")
print(df.isnull().sum())

# Check for duplicate rows
print("\nTOTAL DUPLICATE ROWS:")
print("---------------------")
print(df.duplicated().sum())
