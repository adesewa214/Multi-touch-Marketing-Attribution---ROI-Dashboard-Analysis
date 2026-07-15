# ======================================================
# Project: Multi-Touch Marketing Attribution & ROI Dashboard
# Phase: Data Cleaning
# ======================================================

from pathlib import Path
import pandas as pd

# ======================================================
# PROJECT PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA = BASE_DIR / "data" / "raw" / "multi_touch_attribution_data.csv"

CLEANED_CSV = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.csv"

CLEANED_EXCEL = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.xlsx"

# ======================================================
# LOAD DATASET
# ======================================================

df = pd.read_csv(RAW_DATA)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

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

# ------------------------------------------------------
# 1. Remove leading/trailing spaces
# ------------------------------------------------------

text_columns = ["Channel", "Campaign", "Conversion"]

for col in text_columns:
    df[col] = df[col].str.strip()

# ------------------------------------------------------
# 2. Convert Timestamp to Datetime
# ------------------------------------------------------

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    format="%d-%m-%Y %H:%M"
)

# ------------------------------------------------------
# 3. Standardize Data Types
# ------------------------------------------------------

# User ID -> Integer
df["User ID"] = df["User ID"].astype(int)

# Channel -> Text
df["Channel"] = df["Channel"].astype(str)

# Campaign -> Text
df["Campaign"] = df["Campaign"].astype(str)

# Conversion -> 1 / 0
df["Conversion"] = df["Conversion"].map({
    "Yes": 1,
    "No": 0
}).astype(int)

# ------------------------------------------------------
# 4. Sort records
# ------------------------------------------------------

df = df.sort_values(
    by=["User ID", "Timestamp"]
).reset_index(drop=True)

# ------------------------------------------------------
# 5. Touchpoint Order
# ------------------------------------------------------

df["Touchpoint_Order"] = (
    df.groupby("User ID")
      .cumcount() + 1
)

# ======================================================
# FINAL DATASET SUMMARY
# ======================================================

print("\nCleaning completed successfully!")

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ======================================================
# EXPORT CLEANED DATASET
# ======================================================

df.to_csv(CLEANED_CSV, index=False)

df.to_excel(CLEANED_EXCEL, index=False)

print("\n" + "=" * 60)
print("CLEANED DATASET EXPORTED SUCCESSFULLY")
print("=" * 60)

print(f"\nCSV File   : {CLEANED_CSV}")
print(f"Excel File : {CLEANED_EXCEL}")