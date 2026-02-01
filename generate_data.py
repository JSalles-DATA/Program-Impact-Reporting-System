"""
generate_data.py
----------------
Generates fake community program participation data and saves it as CSV.

This script:
- Creates at least 300 realistic rows
- Uses only standard libraries + pandas
- Requires NO internet
- Automatically creates folders if missing
"""

import os
import random
import csv
from datetime import datetime, timedelta

# -----------------------
# Folder & file setup
# -----------------------
DATA_DIR = "data"
RAW_FILE = os.path.join(DATA_DIR, "raw_program_data.csv")

os.makedirs(DATA_DIR, exist_ok=True)

# -----------------------
# Reference data
# -----------------------
PROGRAMS = [
    (1, "Youth Skills Development", "Youth"),
    (2, "Affordable Housing Support", "Housing"),
    (3, "Community Health Outreach", "Health"),
    (4, "Job Readiness Training", "Employment"),
]

STATUSES = ["Completed", "Dropped", "In Progress"]

NOTES = [
    "Participant showed strong engagement",
    "Attendance was irregular",
    "Excellent improvement observed",
    "Requires follow-up support",
    "Completed all required activities",
    "Left program early",
]

# -----------------------
# Helper function
# -----------------------
def random_date(start_days_ago=365):
    start_date = datetime.today() - timedelta(days=start_days_ago)
    random_days = random.randint(0, start_days_ago)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

# -----------------------
# Data generation
# -----------------------
rows = []

for i in range(300):
    program_id, program_name, category = random.choice(PROGRAMS)
    status = random.choice(STATUSES)

    # Outcome score logic
    if status == "Completed":
        outcome = random.randint(60, 100)
    elif status == "In Progress":
        outcome = random.randint(30, 80)
    else:
        outcome = random.randint(0, 60)

    rows.append({
        "program_id": program_id,
        "program_name": program_name,
        "category": category,
        "participant_id": f"P{1000 + i}",
        "enrollment_date": random_date(),
        "completion_status": status,
        "outcome_score": outcome,
        "notes": random.choice(NOTES)
    })

# -----------------------
# Write CSV
# -----------------------
with open(RAW_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print("✅ Raw program data generated successfully.")
print(f"📁 File saved at: {RAW_FILE}")
