import pandas as pd
import random

departments = ["IT", "HR", "Finance", "Marketing", "Operations"]
positions = ["Data Analyst", "Recruiter", "Finance Analyst", "Marketing Executive", "Operations Associate"]
interview_status = ["Selected", "Rejected", "Pending"]
offer_status = ["Offered", "No Offer", "Pending"]
joining_status = ["Joined", "Not Joined", "Pending"]

data = []

for i in range(1, 501):
    data.append({
        "Candidate_ID": f"C{i:03}",
        "Name": f"Candidate_{i}",
        "Department": random.choice(departments),
        "Position": random.choice(positions),
        "Interview_Status": random.choice(interview_status),
        "Offer_Status": random.choice(offer_status),
        "Joining_Status": random.choice(joining_status)
    })

df = pd.DataFrame(data)
df.to_csv("data/candidates_raw.csv", index=False)
print("Dataset Generated Successfully!")
