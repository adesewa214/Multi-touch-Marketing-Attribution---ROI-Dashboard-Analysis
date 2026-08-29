# ======================================================
# Project: Multi-Touch Marketing Attribution & ROI Dashboard
# Phase: Data Cleaning
# ======================================================

import time
from pathlib import Path

import pandas as pd


# ======================================================
# SCRIPT INFORMATION
# ======================================================

SCRIPT_VERSION = "1.0"
PROJECT_NAME = "Multi-Touch Marketing Attribution & ROI Dashboard"

start_time = time.time()

print("=" * 60)
print(PROJECT_NAME)
print("Phase: Data Cleaning")
print(f"Cleaning Script Version: {SCRIPT_VERSION}")
print("=" * 60)


# ======================================================
# FILE PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = (
    BASE_DIR
    / "data"
    / "raw"
    / "final_multi_touch_attribution_roi_dataset_v2.csv"
)

CSV_OUTPUT = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "cleaned_multi_touch_attribution_data.csv"
)

EXCEL_OUTPUT = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "cleaned_multi_touch_attribution_data.xlsx"
)

REPORT_OUTPUT = (
    BASE_DIR
    / "data"
    / "cleaned"
    / "cleaning_report.txt"
)


# ======================================================
# LOAD DATASET
# ======================================================

df = pd.read_csv(INPUT_FILE)

print("\n" + "=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nDataset Shape:")
print(df.shape)


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
    column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print("\nRequired column validation: PASSED")


# ======================================================
# INITIAL DATASET INFORMATION
# ======================================================

print("\nDataset Information:")
df.info()

memory_usage = (
    df.memory_usage(deep=True).sum()
    / (1024 ** 2)
)

print(f"\nMemory Usage: {memory_usage:.2f} MB")

print("\nFirst Five Rows:")
print(df.head())

print("\nInitial Missing Values:")
print(df.isnull().sum())

initial_duplicates = df.duplicated().sum()

print("\nInitial Duplicate Records:")
print(initial_duplicates)

print("\nStatistical Summary:")
print(df.describe(include="all"))


# ======================================================
# START DATA CLEANING
# ======================================================

print("\n" + "=" * 60)
print("STARTING DATA CLEANING")
print("=" * 60)


# ======================================================
# 1. REMOVE DUPLICATES
# ======================================================

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

duplicates_removed = (
    duplicates_before - duplicates_after
)

print("\nDuplicate Records:")
print(f"Before Cleaning : {duplicates_before}")
print(f"After Cleaning  : {duplicates_after}")
print(f"Removed         : {duplicates_removed}")


# ======================================================
# 2. CLEAN TEXT COLUMNS
# ======================================================

text_columns = [
    "Channel",
    "Campaign",
    "Conversion",
    "Performance_Rating"
]

for column in text_columns:
    df[column] = (
        df[column]
        .astype("string")
        .str.strip()
    )

print("\nText columns cleaned successfully.")


# ======================================================
# 3. HANDLE MISSING CAMPAIGN LABEL
# ======================================================

missing_campaign_count = (
    df["Campaign"]
    .eq("-")
    .sum()
)

df["Campaign"] = df["Campaign"].replace(
    "-",
    "No Campaign"
)

print(
    f"\nCampaign '-' values replaced: "
    f"{missing_campaign_count}"
)


# ======================================================
# 4. CONVERT TIMESTAMP TO DATETIME
# ======================================================

df["Timestamp"] = pd.to_datetime(
    df["Timestamp"],
    dayfirst=True,
    errors="coerce"
)

invalid_timestamp_count = (
    df["Timestamp"].isna().sum()
)

if invalid_timestamp_count > 0:

    print(
        f"\nInvalid timestamps found: "
        f"{invalid_timestamp_count}"
    )

    df = df.dropna(
        subset=["Timestamp"]
    )

else:

    print(
        "\nTimestamp conversion: PASSED"
    )


# ======================================================
# 5. DATASET DATE RANGE
# ======================================================

print("\n" + "=" * 60)
print("DATASET DATE RANGE")
print("=" * 60)

start_date = df["Timestamp"].min()
end_date = df["Timestamp"].max()

total_days = (
    end_date - start_date
).days + 1

print(f"Start Date : {start_date}")
print(f"End Date   : {end_date}")
print(f"Total Days : {total_days}")


# ======================================================
# 6. USER ID DATA TYPE
# ======================================================

df["User ID"] = pd.to_numeric(
    df["User ID"],
    errors="coerce"
)

invalid_user_ids = (
    df["User ID"].isna().sum()
)

if invalid_user_ids > 0:

    print(
        f"\nInvalid User IDs found: "
        f"{invalid_user_ids}"
    )

    df = df.dropna(
        subset=["User ID"]
    )

df["User ID"] = df["User ID"].astype(int)

print("\nUser ID conversion: PASSED")


# ======================================================
# 7. VALIDATE CONVERSION VALUES
# ======================================================

print("\n" + "=" * 60)
print("CONVERSION VALUE VALIDATION")
print("=" * 60)

valid_conversion_values = {
    "Yes",
    "No"
}

actual_conversion_values = set(
    df["Conversion"]
    .dropna()
    .unique()
)

invalid_conversion_values = (
    actual_conversion_values
    - valid_conversion_values
)

if invalid_conversion_values:

    raise ValueError(
        "Unexpected Conversion values found: "
        f"{invalid_conversion_values}"
    )

print(
    "Conversion source values: "
    "PASSED"
)


# ======================================================
# 8. CONVERT CONVERSION TO 1/0
# ======================================================

df["Conversion"] = (
    df["Conversion"]
    .replace(
        {
            "Yes": 1,
            "No": 0
        }
    )
    .astype(int)
)

print(
    "Conversion converted from "
    "Yes/No to 1/0."
)


# ======================================================
# 9. SORT USER JOURNEY
# ======================================================

df = df.sort_values(
    by=[
        "User ID",
        "Timestamp"
    ]
).reset_index(drop=True)


# ======================================================
# 10. CREATE TOUCHPOINT ORDER
# ======================================================

df["Touchpoint_Order"] = (
    df.groupby("User ID")
    .cumcount()
    + 1
)

print(
    "\nTouchpoint order created successfully."
)


# ======================================================
# 11. ROUND NUMERIC VALUES
# ======================================================

numeric_columns = [
    "Campaign_Cost_USD",
    "Budget_USD",
    "Revenue_USD",
    "Profit_USD",
    "ROI_%",
    "ROAS",
    "CPA_USD"
]

for column in numeric_columns:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )

    df[column] = df[column].round(2)

print(
    "\nNumeric columns standardized "
    "and rounded to 2 decimal places."
)


# ======================================================
# 12. FILL MISSING CPA VALUES
# ======================================================

missing_cpa = (
    df["CPA_USD"]
    .isna()
    .sum()
)

df["CPA_USD"] = (
    df["CPA_USD"]
    .fillna(0)
    .round(2)
)

print(
    f"\nMissing CPA values replaced with 0: "
    f"{missing_cpa}"
)


# ======================================================
# 13. RECALCULATE PROFIT
# ======================================================

df["Profit_USD"] = (
    df["Revenue_USD"]
    - df["Campaign_Cost_USD"]
).round(2)

print(
    "\nProfit column recalculated successfully."
)


# ======================================================
# 14. PROFIT VALIDATION
# ======================================================

profit_validation = (
    df["Profit_USD"]
    ==
    (
        df["Revenue_USD"]
        - df["Campaign_Cost_USD"]
    ).round(2)
)

print("\nProfit Validation:")

if profit_validation.all():

    print(
        "PASS : Profit column is correct."
    )

else:

    failed_profit_rows = (
        ~profit_validation
    ).sum()

    print(
        "FAIL : Profit column has "
        "inconsistencies."
    )

    print(
        f"Rows Failed: {failed_profit_rows}"
    )


# ======================================================
# 15. NUMERIC COLUMN VALIDATION
# ======================================================

print("\n" + "=" * 60)
print("NUMERIC COLUMN VALIDATION")
print("=" * 60)

for column in numeric_columns:

    missing_count = (
        df[column]
        .isna()
        .sum()
    )

    print(f"\n{column}")
    print(
        f"Minimum Value : "
        f"{df[column].min()}"
    )

    print(
        f"Maximum Value : "
        f"{df[column].max()}"
    )

    if missing_count == 0:

        print("Status : PASS")

    else:

        print(
            f"Status : FAIL "
            f"({missing_count} missing values)"
        )


# ======================================================
# 16. DATA QUALITY VALIDATION
# ======================================================

print("\n" + "=" * 60)
print("DATA QUALITY VALIDATION")
print("=" * 60)


# Check negative values
negative_value_counts = {}

for column in numeric_columns:

    negative_count = (
        df[column] < 0
    ).sum()

    negative_value_counts[column] = (
        negative_count
    )

    print(
        f"{column}: "
        f"{negative_count} negative value(s)"
    )


# Validate Conversion
valid_conversion = (
    df["Conversion"]
    .isin([0, 1])
    .all()
)

if valid_conversion:

    print(
        "\nConversion column validation: "
        "PASSED"
    )

else:

    print(
        "\nConversion column validation: "
        "FAILED"
    )


# Validate Timestamp
missing_timestamp = (
    df["Timestamp"].isna().sum()
)

print(
    f"Missing Timestamp values: "
    f"{missing_timestamp}"
)


# ======================================================
# 17. FINAL DATASET INFORMATION
# ======================================================

print("\n" + "=" * 60)
print("FINAL DATASET INFORMATION")
print("=" * 60)

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nFinal Dataset Shape:")
print(df.shape)

final_missing_values = (
    df.isnull().sum()
)

print("\nMissing Values After Cleaning:")
print(final_missing_values)

total_remaining_missing = (
    final_missing_values.sum()
)


# ======================================================
# 18. CLEANED DATASET STATISTICS
# ======================================================

print("\n" + "=" * 60)
print("CLEANED DATASET STATISTICS")
print("=" * 60)

unique_users = (
    df["User ID"].nunique()
)

unique_channels = (
    df["Channel"].nunique()
)

unique_campaigns = (
    df["Campaign"].nunique()
)

successful_conversions = (
    df["Conversion"].sum()
)

total_touchpoints = len(df)

print(
    f"Unique Users           : "
    f"{unique_users}"
)

print(
    f"Unique Channels        : "
    f"{unique_channels}"
)

print(
    f"Unique Campaigns       : "
    f"{unique_campaigns}"
)

print(
    f"Successful Conversions : "
    f"{successful_conversions}"
)

print(
    f"Total Touchpoints      : "
    f"{total_touchpoints}"
)

print("\nChannel Distribution:")
print(
    df["Channel"]
    .value_counts()
)

print("\nPerformance Rating Distribution:")
print(
    df["Performance_Rating"]
    .value_counts()
)


# ======================================================
# 19. CHANNEL-WISE CONVERSION SUMMARY
# ======================================================

print("\n" + "=" * 60)
print("CHANNEL-WISE CONVERSION SUMMARY")
print("=" * 60)

channel_summary = (
    df.groupby("Channel")
    .agg(
        Total_Touchpoints=(
            "User ID",
            "count"
        ),
        Total_Conversions=(
            "Conversion",
            "sum"
        )
    )
)

channel_summary[
    "Conversion_Rate_%"
] = (
    channel_summary[
        "Total_Conversions"
    ]
    /
    channel_summary[
        "Total_Touchpoints"
    ]
    * 100
).round(2)

print(channel_summary)


# ======================================================
# 20. FINAL CLEANING SUMMARY
# ======================================================

print("\n" + "=" * 60)
print("DATA CLEANING SUMMARY")
print("=" * 60)

print(
    f"Initial Records          : "
    f"{len(df) + duplicates_removed}"
)

print(
    f"Final Records            : "
    f"{len(df)}"
)

print(
    f"Duplicate Records Removed: "
    f"{duplicates_removed}"
)

print(
    f"Missing CPA Filled       : "
    f"{missing_cpa}"
)

print(
    f"Remaining Missing Values : "
    f"{total_remaining_missing}"
)

print(
    "Profit Validation        : "
    f"{'PASSED' if profit_validation.all() else 'FAILED'}"
)

print(
    "Conversion Validation    : "
    f"{'PASSED' if valid_conversion else 'FAILED'}"
)

print(
    "\nDataset is ready for:"
)

print(
    "- SQL Analysis"
)

print(
    "- Dashboard Development"
)

print(
    "- ROI & Marketing Attribution Analysis"
)


# ======================================================
# 21. EXPORT CLEANED DATASET
# ======================================================

CSV_OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

print("\n" + "=" * 60)
print("EXPORTING CLEANED DATASET")
print("=" * 60)

df.to_csv(
    CSV_OUTPUT,
    index=False,
    encoding="utf-8-sig"
)

df.to_excel(
    EXCEL_OUTPUT,
    index=False
)

print(
    "\nCSV and Excel files generated successfully."
)

print(
    f"\nCSV File   : {CSV_OUTPUT}"
)

print(
    f"Excel File : {EXCEL_OUTPUT}"
)


# ======================================================
# 22. GENERATE CLEANING REPORT
# ======================================================

with open(
    REPORT_OUTPUT,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "MULTI-TOUCH MARKETING "
        "ATTRIBUTION & ROI DASHBOARD\n"
    )

    report.write(
        "DATA CLEANING REPORT\n"
    )

    report.write(
        "=" * 60 + "\n\n"
    )

    report.write(
        f"Script Version           : "
        f"{SCRIPT_VERSION}\n"
    )

    report.write(
        f"Initial Records          : "
        f"{len(df) + duplicates_removed}\n"
    )

    report.write(
        f"Final Records            : "
        f"{len(df)}\n"
    )

    report.write(
        f"Duplicate Records Removed: "
        f"{duplicates_removed}\n"
    )

    report.write(
        f"Missing CPA Filled       : "
        f"{missing_cpa}\n"
    )

    report.write(
        f"Remaining Missing Values : "
        f"{total_remaining_missing}\n"
    )

    report.write(
        f"Unique Users             : "
        f"{unique_users}\n"
    )

    report.write(
        f"Unique Channels          : "
        f"{unique_channels}\n"
    )

    report.write(
        f"Unique Campaigns         : "
        f"{unique_campaigns}\n"
    )

    report.write(
        f"Successful Conversions   : "
        f"{successful_conversions}\n"
    )

    report.write(
        f"Total Touchpoints        : "
        f"{total_touchpoints}\n"
    )

    report.write(
        f"Dataset Start Date       : "
        f"{start_date}\n"
    )

    report.write(
        f"Dataset End Date         : "
        f"{end_date}\n"
    )

    report.write(
        f"Total Days               : "
        f"{total_days}\n"
    )

    report.write(
        "\nProfit Validation        : "
        f"{'PASSED' if profit_validation.all() else 'FAILED'}\n"
    )

    report.write(
        "Conversion Validation    : "
        f"{'PASSED' if valid_conversion else 'FAILED'}\n"
    )


# ======================================================
# 23. EXECUTION SUMMARY
# ======================================================

end_time = time.time()

execution_time = (
    end_time - start_time
)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print(
    f"\nCleaning Report : "
    f"{REPORT_OUTPUT}"
)

print(
    f"Execution Time  : "
    f"{execution_time:.2f} seconds"
)

print(
    "\nDataset is validated and ready "
    "for SQL analysis and dashboard development."
)