# ======================================================
# Project: Multi-Touch Marketing Attribution & ROI Dashboard
# Phase: Data Cleaning
# ======================================================

from pathlib import Path
import pandas as pd

# ======================================================
# FILE PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "final_multi_touch_attribution_roi_dataset_v2.csv"

CSV_OUTPUT = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.csv"

EXCEL_OUTPUT = BASE_DIR / "data" / "cleaned" / "cleaned_multi_touch_attribution_data.xlsx"

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nFirst Five Rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nStatistical Summary:")
print(df.describe(include="all"))

# ======================================================
# DATA CLEANING
# ======================================================

print("\n" + "=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)

# -----------------------------
# Remove duplicate rows
# -----------------------------
df = df.drop_duplicates()

# -----------------------------
# Trim spaces
# -----------------------------
text_columns = [
    "Channel",
    "Campaign",
    "Conversion",
    "Performance_Rating"
]

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# -----------------------------
# Replace '-' campaign
# -----------------------------
df["Campaign"] = df["Campaign"].replace("-", "No Campaign")

# -----------------------------
# Timestamp -> Datetime
# -----------------------------
df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    dayfirst=True,
    errors="coerce"
)

# Remove invalid timestamps
df = df.dropna(subset=["Timestamp"])

# -----------------------------
# User ID Integer
# -----------------------------
df["User ID"] = df["User ID"].astype(int)

# -----------------------------
# Conversion Yes/No -> 1/0
# -----------------------------
df["Conversion"] = (
    df["Conversion"]
      .replace({
          "Yes": 1,
          "No": 0
      })
      .astype(int)
)

# -----------------------------
# Sort user journey
# -----------------------------
df = df.sort_values(
    by=["User ID", "Timestamp"]
)

# -----------------------------
# Touchpoint Order
# -----------------------------
df["Touchpoint_Order"] = (
    df.groupby("User ID")
      .cumcount()
      + 1
)

# ======================================================
# ROUND NUMERIC VALUES
# ======================================================

money_columns = [
    "Campaign_Cost_USD",
    "Budget_USD",
    "Revenue_USD",
    "ROI_%",
    "ROAS",
    "CPA_USD"
]

for col in money_columns:
    df[col] = df[col].round(2)

# ======================================================
# FIX PROFIT
# ======================================================

df["Profit_USD"] = (
    df["Revenue_USD"]
    - df["Campaign_Cost_USD"]
).round(2)

# ======================================================
# VALIDATION
# ======================================================

validation = (
    df["Profit_USD"]
    ==
    (df["Revenue_USD"] - df["Campaign_Cost_USD"]).round(2)
)

print("\nProfit Validation:")

if validation.all():
    print("PASS : Profit column is correct.")
else:
    print("FAIL : Profit column has inconsistencies.")
    print("Rows Failed:", (~validation).sum())

# ======================================================
# FINAL DATA TYPES
# ======================================================

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
# -----------------------------
# Fill missing CPA values with 0
# -----------------------------
df["CPA_USD"] = df["CPA_USD"].fillna(0).round(2)

# ======================================================
# EXPORT
# ======================================================

CSV_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(
    CSV_OUTPUT,
    index=False
)

df.to_excel(
    EXCEL_OUTPUT,
    index=False
)

print("\n" + "=" * 60)
print("CLEANED DATASET EXPORTED SUCCESSFULLY")
print("=" * 60)

print(f"\nCSV File   : {CSV_OUTPUT}")
print(f"Excel File : {EXCEL_OUTPUT}")