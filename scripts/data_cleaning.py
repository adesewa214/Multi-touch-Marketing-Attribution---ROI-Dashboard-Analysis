# ======================================================
# Project: Multi-Touch Marketing Attribution & ROI Dashboard
# Phase: Data Cleaning
# ======================================================

from pathlib import Path
import pandas as pd

# ======================================================
# LOAD DATASET
# ======================================================

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset path
DATA_PATH = BASE_DIR / "data" / "raw" / "multi_touch_attribution_data.csv"

# Load dataset
df = pd.read_csv(DATA_PATH)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

# ======================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# ======================================================

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nFirst Five Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nUnique Channels:")
print(df["Channel"].unique())

print("\nUnique Campaigns:")
print(df["Campaign"].unique())

print("\nConversion Values:")
print(df["Conversion"].unique())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# ======================================================
# DATA CLEANING
# ======================================================

print("\n" + "=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)

# Convert Timestamp from string to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Remove leading/trailing spaces
text_columns = ["Channel", "Campaign", "Conversion"]

for col in text_columns:
    df[col] = df[col].str.strip()

# Check where '-' exists
print("\nRows containing '-' in Campaign:")
print(df[df["Campaign"] == "-"]["Channel"].value_counts())

# Replace '-' with 'No Campaign'
df["Campaign"] = df["Campaign"].replace("-", "No Campaign")

# Sort customer journey chronologically
df = df.sort_values(
    by=["User ID", "Timestamp"]
).reset_index(drop=True)

# ======================================================
# FEATURE ENGINEERING
# ======================================================

df["Date"] = df["Timestamp"].dt.date
df["Year"] = df["Timestamp"].dt.year
df["Month"] = df["Timestamp"].dt.month_name()
df["Day"] = df["Timestamp"].dt.day_name()
df["Hour"] = df["Timestamp"].dt.hour

# ======================================================
# FINAL VALIDATION
# ======================================================

print("\nCleaning completed successfully!")

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nUpdated Campaign Values:")
print(df["Campaign"].unique())

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ======================================================
# EXPORT CLEANED DATASET
# ======================================================

CSV_OUTPUT = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.csv"
EXCEL_OUTPUT = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.xlsx"

# Export CSV
df.to_csv(CSV_OUTPUT, index=False)

# Export Excel
df.to_excel(EXCEL_OUTPUT, index=False)

print("\n" + "=" * 60)
print("CLEANED DATASET EXPORTED SUCCESSFULLY")
print("=" * 60)

print(f"\nCSV File   : {CSV_OUTPUT}")
print(f"Excel File : {EXCEL_OUTPUT}")