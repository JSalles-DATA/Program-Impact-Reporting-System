"""
clean_data.py
-------------
Cleans raw program data and saves a validated version.

This script:
- Removes duplicates
- Handles missing values
- Ensures outcome_score is between 0 and 100
- Prints a clear data quality summary
"""

import os
import pandas as pd

# -----------------------
# File paths
# -----------------------
DATA_DIR = "data"
RAW_FILE = os.path.join(DATA_DIR, "raw_program_data.csv")
CLEAN_FILE = os.path.join(DATA_DIR, "clean_program_data.csv")

# Defensive check
if not os.path.exists(RAW_FILE):
    raise FileNotFoundError("Raw data file not found. Run generate_data.py first.")

# -----------------------
# Load data
# -----------------------
df = pd.read_csv(RAW_FILE)

original_rows = len(df)

# -----------------------
# Cleaning steps
# -----------------------
df = df.drop_duplicates()

# Fill missing text fields safely
df["notes"] = df["notes"].fillna("No notes provided")
df["completion_status"] = df["completion_status"].fillna("Unknown")
df["category"] = df["category"].fillna("Unknown")

# Ensure outcome_score is numeric and valid
df["outcome_score"] = pd.to_numeric(df["outcome_score"], errors="coerce")
df = df[(df["outcome_score"] >= 0) & (df["outcome_score"] <= 100)]

cleaned_rows = len(df)

# -----------------------
# Save cleaned data
# -----------------------
df.to_csv(CLEAN_FILE, index=False)

# -----------------------
# Summary output
# -----------------------
print("🧹 DATA CLEANING SUMMARY")
print("------------------------")
print(f"Original rows: {original_rows}")
print(f"Cleaned rows : {cleaned_rows}")
print(f"Removed rows : {original_rows - cleaned_rows}")
print(f"✅ Clean data saved to: {CLEAN_FILE}")
