import pandas as pd

# 1. Load the raw data
df = pd.read_csv("data/candidates_raw.csv")

# 2. Drop duplicates if any exist
df.drop_duplicates(inplace=True)

# 3. Fill missing values with "Unknown" if any exist
df.fillna("Unknown", inplace=True)

# 4. Save the cleaned data as an Excel file
df.to_excel("data/candidates_cleaned.xlsx", index=False)

print("Cleaning Complete")
