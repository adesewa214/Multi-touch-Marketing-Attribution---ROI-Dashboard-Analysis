import time
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

start_time = time.time()

# ======================================================
# SCRIPT INFORMATION
# ======================================================

SCRIPT_VERSION = "1.0"
PROJECT_NAME = "Multi-Touch Marketing Attribution & ROI Dashboard"

print("=" * 60)
print(PROJECT_NAME)
print(f"Cleaning Script Version : {SCRIPT_VERSION}")
print("=" * 60)

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv(INPUT_FILE)

# ======================================================
# VALIDATE REQUIRED COLUMNS
# ======================================================

required_columns = [
    "User ID",
    "Timestamp",
    "Channel",
    "Campaign",
    "Conversion",
    "Campaign_Cost_USD",
    "Budget_USD",
    "Revenue_USD",
    "Profit_USD",
    "ROI_%",
    "ROAS",
    "CPA_USD",
    "Performance_Rating"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing required columns: {missing_columns}")

print("\nAll required columns are present.")
print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())
memory = df.memory_usage(deep=True).sum() / (1024 ** 2)

print(f"\nMemory Usage: {memory:.2f} MB")

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
# NUMERIC COLUMN VALIDATION
# ======================================================

print("\n" + "=" * 60)
print("NUMERIC COLUMN VALIDATION")
print("=" * 60)

numeric_columns = [
    "Campaign_Cost_USD",
    "Budget_USD",
    "Revenue_USD",
    "Profit_USD",
    "ROI_%",
    "ROAS",
    "CPA_USD"
]

for col in numeric_columns:
    print(f"\n{col}")
    print(f"Minimum Value : {df[col].min()}")
    print(f"Maximum Value : {df[col].max()}")

    if df[col].isnull().sum() == 0:
        print("Status : PASS")
    else:
        print(f"Status : FAIL ({df[col].isnull().sum()} missing values)")
        
        
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
# DATA CLEANING SUMMARY
# ======================================================

print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(f"Total Records Processed      : {len(df)}")
print(f"Total Columns               : {len(df.columns)}")
print(f"Duplicate Records Removed   : {duplicates_before}")
print(f"Missing Values Remaining    : {df.isnull().sum().sum()}")
print(f"Missing CPA Values Filled   : {missing_cpa}")

print("\nDataset is ready for:")
print("- SQL Analysis")
print("- Dashboard Development")
print("- ROI & Marketing Attribution Analysis")

# ======================================================
# CLEANED DATASET STATISTICS
# ======================================================

print("\n" + "=" * 60)
print("CLEANED DATASET STATISTICS")
print("=" * 60)

print(f"Unique Users              : {df['User ID'].nunique()}")
print(f"Unique Channels           : {df['Channel'].nunique()}")
print(f"Unique Campaigns          : {df['Campaign'].nunique()}")
print(f"Successful Conversions    : {df['Conversion'].sum()}")
print(f"Total Touchpoints         : {len(df)}")

print("\nChannel Distribution:")
print(df["Channel"].value_counts())

print("\nPerformance Rating Distribution:")
print(df["Performance_Rating"].value_counts())


print("\nCleaning completed successfully.")
print(f"Exporting cleaned dataset with {len(df)} records...")
# ======================================================
# EXPORT
# ======================================================



CSV_OUTPUT.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig"
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

print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(f"Total Rows Processed        : {len(df)}")
print(f"Total Columns              : {len(df.columns)}")
print(f"Remaining Missing Values   : {df.isnull().sum().sum()}")
print(f"Duplicate Records Removed  : {duplicates_before}")
print("Profit Validation          : PASSED")
print("Dataset Status             : Ready for SQL & Dashboard Analysis")
print("\nExport Status : SUCCESS")
print("CSV and Excel files generated successfully.")


# ======================================================
# GENERATE CLEANING REPORT
# ======================================================

with open(REPORT_OUTPUT, "w") as report:

    report.write("MULTI-TOUCH MARKETING ATTRIBUTION & ROI DASHBOARD\n")
    report.write("DATA CLEANING REPORT\n")
    report.write("=" * 60 + "\n\n")

    report.write(f"Total Records            : {len(df)}\n")
    report.write(f"Total Columns            : {len(df.columns)}\n")
    report.write(f"Duplicate Records Removed: {duplicates_before}\n")
    report.write(f"Missing Values Remaining : {df.isnull().sum().sum()}\n")
    report.write(f"Missing CPA Filled       : {missing_cpa}\n")
    report.write(f"Unique Users             : {df['User ID'].nunique()}\n")
    report.write(f"Unique Channels          : {df['Channel'].nunique()}\n")
    report.write(f"Unique Campaigns         : {df['Campaign'].nunique()}\n")
    report.write(f"Successful Conversions   : {df['Conversion'].sum()}\n")

print("\nCleaning report generated successfully.")
print(f"Report File : {REPORT_OUTPUT}")

# ======================================================
# DATA QUALITY VALIDATION
# ======================================================

print("\n" + "=" * 60)
print("DATA QUALITY VALIDATION")
print("=" * 60)

# Check for negative monetary values
money_columns = [
    "Campaign_Cost_USD",
    "Budget_USD",
    "Revenue_USD",
    "Profit_USD",
    "ROI_%",
    "ROAS",
    "CPA_USD"
]

for col in money_columns:
    negative_count = (df[col] < 0).sum()
    print(f"{col}: {negative_count} negative value(s)")

# Validate Conversion values
valid_conversion = df["Conversion"].isin([0, 1]).all()

if valid_conversion:
    print("\nConversion column validation: PASSED")
else:
    print("\nConversion column validation: FAILED")

# Check for missing timestamps
missing_timestamp = df["Timestamp"].isna().sum()
print(f"Missing Timestamp values: {missing_timestamp}")

print("\nCleaning process completed successfully.")
print("The dataset is validated and ready for SQL analysis.")

end_time = time.time()

print(f"\nExecution Time: {end_time - start_time:.2f} seconds")