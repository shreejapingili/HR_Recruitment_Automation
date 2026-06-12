import pandas as pd
import random

# Load the dataset
df = pd.read_excel("data/candidates_cleaned.xlsx")

start_date = pd.to_datetime("2026-01-01")
end_date = pd.to_datetime("2026-06-01")
days_range = (end_date - start_date).days

random.seed(42)

# Generate dates directly as clean "YYYY-MM-DD" text strings
df["Application_Date"] = [
    (start_date + pd.to_timedelta(random.randint(0, days_range), unit="D")).strftime("%Y-%m-%d") 
    for _ in range(len(df))
]

df.to_excel("data/candidates_cleaned.xlsx", index=False)
print("Dates successfully updated to clean YYYY-MM-DD format!")
