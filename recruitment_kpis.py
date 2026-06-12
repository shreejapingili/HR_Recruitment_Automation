import pandas as pd

# Load the cleaned Excel dataset
df = pd.read_excel("data/candidates_cleaned.xlsx")

# Calculate volumes
total_applications = len(df)
selected = len(df[df["Interview_Status"] == "Selected"])
offers = len(df[df["Offer_Status"] == "Offered"])
joined = len(df[df["Joining_Status"] == "Joined"])

# Calculate performance percentages
conversion_rate = (selected / total_applications) * 100
offer_acceptance = (joined / offers) * 100 if offers > 0 else 0

# Print the KPI Dashboard
print("\n=== RECRUITMENT KPI DASHBOARD ===")
print(f"Total Applications: {total_applications}")
print(f"Selected:           {selected}")
print(f"Offers Extended:    {offers}")
print(f"Joined:             {joined}")
print(f"Conversion Rate:    {round(conversion_rate, 2)}%")
print(f"Offer Acceptance:   {round(offer_acceptance, 2)}%")
print("=================================\n")
