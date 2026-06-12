summary = """
Recruitment Summary

Total Applications: 500

Selected Candidates: 180

Offers Released: 100

Joined Candidates: 85
"""

# Write the multi-line string to a text file
with open("reports/recruiter_summary.txt", "w") as file:
    file.write(summary)

print("Summary Generated")
