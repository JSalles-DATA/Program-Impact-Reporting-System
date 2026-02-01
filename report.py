"""
report.py
---------
Analyzes cleaned program data and generates reports and charts.

This script:
- Calculates key performance indicators
- Generates PNG charts using matplotlib
- Prints a clear, human-readable summary
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# Paths
# -----------------------
DATA_DIR = "data"
REPORT_DIR = "reports"
CLEAN_FILE = os.path.join(DATA_DIR, "clean_program_data.csv")

os.makedirs(REPORT_DIR, exist_ok=True)

if not os.path.exists(CLEAN_FILE):
    raise FileNotFoundError("Clean data not found. Run clean_data.py first.")

# -----------------------
# Load data
# -----------------------
df = pd.read_csv(CLEAN_FILE)

# -----------------------
# Calculations
# -----------------------
total_participants = df["participant_id"].nunique()

completion_counts = df["completion_status"].value_counts()
completed = completion_counts.get("Completed", 0)
completion_rate = (completed / total_participants) * 100

avg_outcome_by_category = df.groupby("category")["outcome_score"].mean()

# -----------------------
# Chart 1: Completion Status
# -----------------------
plt.figure()
completion_counts.plot(kind="bar")
plt.title("Completion Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Participants")
plt.tight_layout()
plt.savefig(os.path.join(REPORT_DIR, "completion_status_distribution.png"))
plt.close()

# -----------------------
# Chart 2: Average Outcome Score
# -----------------------
plt.figure()
avg_outcome_by_category.plot(kind="bar")
plt.title("Average Outcome Score by Category")
plt.xlabel("Program Category")
plt.ylabel("Average Outcome Score")
plt.tight_layout()
plt.savefig(os.path.join(REPORT_DIR, "average_outcome_by_category.png"))
plt.close()

# -----------------------
# Terminal Report
# -----------------------
print("\n📊 PROGRAM IMPACT REPORT")
print("------------------------")
print(f"Total participants      : {total_participants}")
print(f"Completion rate         : {completion_rate:.2f}%")
print("\nAverage Outcome Score by Category:")
for category, score in avg_outcome_by_category.items():
    print(f" - {category}: {score:.1f}")

print("\n📁 Reports saved in the 'reports/' folder")
