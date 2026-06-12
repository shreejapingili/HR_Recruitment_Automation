import pandas as pd

# Read the generated CSV file
df = pd.read_csv("data/candidates_raw.csv")

# Print the first 5 rows
print(df.head())
