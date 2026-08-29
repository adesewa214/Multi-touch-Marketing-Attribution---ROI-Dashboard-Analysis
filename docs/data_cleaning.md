# Data Cleaning Documentation

## 1. Overview

Data cleaning and preparation were performed to ensure that the Multi-Touch Marketing Attribution dataset was structured, consistent, and suitable for further analysis.

The cleaned dataset serves as the foundation for:

* Marketing attribution analysis
* SQL analysis
* KPI calculations
* Dashboard development
* Channel performance analysis
* Campaign performance analysis
* Customer journey analysis

The data cleaning process was implemented using Python and pandas.

The main cleaning script is located at:

```text
scripts/data_cleaning.py
```

---

## 2. Raw Dataset

The raw dataset is stored at:

```text
data/raw/multi_touch_attribution_data.csv
```

The initial dataset contained:

* **10,000 rows**
* **5 columns**

The original columns were:

| Column     | Description                                                |
| ---------- | ---------------------------------------------------------- |
| User ID    | Unique identifier associated with a user                   |
| Timestamp  | Date and time when the marketing interaction occurred      |
| Channel    | Marketing channel associated with the interaction          |
| Campaign   | Marketing campaign associated with the interaction         |
| Conversion | Indicates whether the interaction resulted in a conversion |

---

# 3. Data Cleaning Objectives

The main objectives of the data cleaning process were to:

1. Load and inspect the raw dataset.
2. Check the dataset shape.
3. Review column names.
4. Inspect data types.
5. Check for missing values.
6. Inspect unique values in important categorical columns.
7. Convert the `Timestamp` column to datetime format.
8. Standardize invalid or unclear campaign values.
9. Create additional date and time features.
10. Add touchpoint ordering information.
11. Validate the cleaned dataset.
12. Export the final cleaned dataset in CSV and Excel formats.

---

# 4. Loading the Dataset

The raw dataset was loaded using pandas.

The project uses file paths based on the project directory structure to ensure that the script can be executed consistently.

The raw dataset path is:

```text
data/raw/multi_touch_attribution_data.csv
```

After loading the dataset, its structure was inspected before applying any transformations.

---

# 5. Initial Data Inspection

The dataset was inspected to understand its structure and contents.

The following checks were performed:

* Dataset shape
* Column names
* Data types
* Missing values
* Unique channel values
* Unique campaign values
* Conversion values

The initial dataset shape was:

```text
Rows: 10,000
Columns: 5
```

---

# 6. Original Dataset Columns

The raw dataset contained the following columns:

```text
User ID
Timestamp
Channel
Campaign
Conversion
```

These columns represent individual marketing touchpoints associated with users.

A single user may appear multiple times because users can interact with more than one marketing channel.

For example:

```text
User A
   ↓
Email
   ↓
Social Media
   ↓
Search Ads
   ↓
Conversion
```

This structure supports multi-touch marketing attribution analysis.

---

# 7. Data Type Inspection

The data types of all columns were reviewed before cleaning.

The most important transformation involved the `Timestamp` column.

Initially, the timestamp information was stored as text rather than a proper datetime data type.

This limited the ability to perform:

* Date-based analysis
* Monthly analysis
* Daily analysis
* Hourly analysis
* Chronological ordering
* Time-based dashboard filtering

Therefore, the `Timestamp` column was converted to datetime format.

---

# 8. Timestamp Conversion

The `Timestamp` column was converted from text/string format into a datetime format.

### Before Cleaning

```text
Timestamp → Text/String
```

### After Cleaning

```text
Timestamp → Datetime
```

This transformation allows the dataset to be used for chronological and time-based analysis.

The cleaned timestamp can be used to identify:

* Date
* Year
* Month
* Day
* Hour

---

# 9. Date and Time Feature Engineering

After converting the `Timestamp` column to datetime format, additional columns were created.

The following features were extracted:

| New Column | Description                               |
| ---------- | ----------------------------------------- |
| Date       | Calendar date extracted from Timestamp    |
| Year       | Year extracted from Timestamp             |
| Month      | Month extracted from Timestamp            |
| Day        | Day of the month extracted from Timestamp |
| Hour       | Hour extracted from Timestamp             |

These fields simplify downstream analysis and dashboard development.

---

## 9.1 Date

The `Date` column represents the calendar date of each marketing touchpoint.

It can be used for:

* Daily analysis
* Date filtering
* Trend analysis

---

## 9.2 Year

The `Year` column represents the year extracted from the timestamp.

It can be used to:

* Compare yearly performance
* Filter data by year
* Analyze long-term trends

---

## 9.3 Month

The `Month` column represents the month extracted from the timestamp.

It can be used for:

* Monthly conversion analysis
* Monthly revenue analysis
* Monthly campaign performance
* Seasonal trend analysis

---

## 9.4 Day

The `Day` column represents the day of the month.

It can support:

* Daily performance analysis
* Short-term campaign monitoring
* Identification of high-activity days

---

## 9.5 Hour

The `Hour` column represents the hour when a marketing touchpoint occurred.

It can be used to analyze:

* Hourly interaction patterns
* Peak activity periods
* Time-based customer engagement

---

# 10. Campaign Value Inspection

The `Campaign` column was inspected to identify all unique campaign values.

The dataset contained the following campaign categories:

* New Product Launch
* Winter Sale
* Brand Awareness
* Retargeting
* Discount Offer
* `-`

The value `-` was identified as a placeholder rather than a meaningful campaign name.

Therefore, it required standardization.

---

# 11. Campaign Value Standardization

The placeholder value:

```text
-
```

was replaced with:

```text
No Campaign
```

This transformation improves the readability and consistency of the dataset.

Instead of treating `-` as an actual campaign, records are now clearly identified as touchpoints without a specific campaign.

---

## 11.1 Records with No Campaign

Before standardization, the `-` campaign values were inspected by marketing channel.

The identified counts were:

| Channel        | Records with `-` Campaign |
| -------------- | ------------------------: |
| Direct Traffic |                     1,721 |
| Email          |                       303 |
| Social Media   |                       285 |
| Display Ads    |                       281 |
| Referral       |                       277 |
| Search Ads     |                       264 |

The total number of placeholder campaign records was therefore:

```text
3,131
```

These values were standardized to `No Campaign`.

---

# 12. Final Campaign Categories

After cleaning, the `Campaign` column contained the following categories:

```text
Discount Offer
No Campaign
New Product Launch
Brand Awareness
Retargeting
Winter Sale
```

This provides a more meaningful and consistent representation of campaign information.

---

# 13. Channel Validation

The `Channel` column was inspected to verify the available marketing channels.

The dataset contains six channels:

* Email
* Search Ads
* Social Media
* Direct Traffic
* Referral
* Display Ads

No unnecessary channel categories were introduced during the cleaning process.

These channels were retained for further analysis.

---

# 14. Conversion Value Validation

The `Conversion` column was inspected to verify its available values.

The dataset contains:

```text
Yes
No
```

These values were retained because they provide the conversion status for each marketing interaction.

The `Conversion` field is later used for calculations such as:

* Total conversions
* Conversion rate
* Channel conversion analysis
* Campaign conversion analysis

---

# 15. Touchpoint Order Creation

A new column called:

```text
Touchpoint_Order
```

was added to the cleaned dataset.

The purpose of this column is to support multi-touch customer journey analysis.

Because a user can have multiple interactions with different marketing channels, the touchpoint order helps identify the sequence of those interactions.

For example:

```text
User A

Touchpoint 1 → Email
Touchpoint 2 → Social Media
Touchpoint 3 → Search Ads
Touchpoint 4 → Conversion
```

This information can support analysis such as:

* First-touch analysis
* Subsequent touchpoint analysis
* Customer journey analysis
* Number of interactions before conversion
* Marketing attribution analysis

---

# 16. Missing Value Validation

Missing values were checked during and after the cleaning process.

The final cleaned dataset contained no missing values in the required columns.

| Column           | Missing Values |
| ---------------- | -------------: |
| User ID          |              0 |
| Timestamp        |              0 |
| Channel          |              0 |
| Campaign         |              0 |
| Conversion       |              0 |
| Touchpoint_Order |              0 |
| Date             |              0 |
| Year             |              0 |
| Month            |              0 |
| Day              |              0 |
| Hour             |              0 |

This confirms that the required fields in the cleaned dataset are complete.

---

# 17. Final Dataset Structure

After the cleaning and feature engineering process, the final dataset contained:

* **10,000 rows**
* **11 columns**

The final columns are:

```text
User ID
Timestamp
Channel
Campaign
Conversion
Touchpoint_Order
Date
Year
Month
Day
Hour
```

---

# 18. Data Cleaning Summary

The complete data cleaning workflow can be summarized as follows:

| Step | Action                               |
| ---- | ------------------------------------ |
| 1    | Loaded the raw CSV dataset           |
| 2    | Checked dataset shape                |
| 3    | Reviewed column names                |
| 4    | Inspected data types                 |
| 5    | Checked missing values               |
| 6    | Inspected unique channel values      |
| 7    | Inspected unique campaign values     |
| 8    | Inspected conversion values          |
| 9    | Converted `Timestamp` to datetime    |
| 10   | Created the `Date` column            |
| 11   | Created the `Year` column            |
| 12   | Created the `Month` column           |
| 13   | Created the `Day` column             |
| 14   | Created the `Hour` column            |
| 15   | Identified `-` values in `Campaign`  |
| 16   | Replaced `-` with `No Campaign`      |
| 17   | Added `Touchpoint_Order`             |
| 18   | Validated missing values             |
| 19   | Verified the final dataset structure |
| 20   | Exported the cleaned dataset         |

---

# 19. Final Data Quality Checks

After completing the transformations, the dataset was validated.

The following checks were performed:

### Dataset Shape

The final dataset contained:

```text
10,000 rows
11 columns
```

### Missing Values

All required columns contained:

```text
0 missing values
```

### Campaign Values

The placeholder value `-` was replaced with:

```text
No Campaign
```

### Timestamp

The timestamp was successfully converted to a datetime data type.

### Additional Features

The following columns were successfully added:

```text
Touchpoint_Order
Date
Year
Month
Day
Hour
```

---

# 20. Exporting the Cleaned Dataset

After the cleaning process was completed, the dataset was exported in two formats.

## CSV Output

```text
data/cleaned/cleaned_multi_touch_attribution_data.csv
```

The CSV file is used for:

* Data analysis
* SQL processing
* Dashboard development
* Further data processing

---

## Excel Output

```text
data/cleaned/cleaned_multi_touch_attribution_data.xlsx
```

The Excel file is useful for:

* Manual inspection
* Data review
* Sharing with team members
* Quick analysis

---

# 21. Data Pipeline

The overall data preparation process can be represented as:

```text
Raw Dataset
     ↓
Data Loading
     ↓
Initial Data Inspection
     ↓
Data Type Validation
     ↓
Timestamp Conversion
     ↓
Date and Time Feature Creation
     ↓
Campaign Value Inspection
     ↓
Campaign Standardization
     ↓
Touchpoint Order Creation
     ↓
Missing Value Validation
     ↓
Final Data Quality Checks
     ↓
Cleaned Dataset
     ↓
CSV and Excel Export
```

---

# 22. Reproducibility

The cleaning process is designed to be reproducible.

The raw dataset remains separate from the cleaned output.

### Raw Data

```text
data/raw/multi_touch_attribution_data.csv
```

### Cleaning Script

```text
scripts/data_cleaning.py
```

### Cleaned Data

```text
data/cleaned/cleaned_multi_touch_attribution_data.csv
```

```text
data/cleaned/cleaned_multi_touch_attribution_data.xlsx
```

To reproduce the cleaning process, run:

```bash
python scripts/data_cleaning.py
```

The script applies the required transformations and generates the cleaned output files.

---

# 23. Project Folder Structure

The relevant project structure is:

```text
Multi-touch-Marketing-Attribution---ROI-Dashboard-Analysis/
│
├── data/
│   ├── raw/
│   │   └── multi_touch_attribution_data.csv
│   │
│   └── cleaned/
│       ├── cleaned_multi_touch_attribution_data.csv
│       └── cleaned_multi_touch_attribution_data.xlsx
│
├── scripts/
│   └── data_cleaning.py
│
└── docs/
    └── data_cleaning.md
```

This structure keeps:

* Raw data separate from processed data
* Cleaning logic separate from datasets
* Documentation separate from analysis files

---

# 24. Importance of the Cleaning Process

The data cleaning process ensures that the dataset is suitable for reliable analysis.

The cleaning stage improves:

* Data consistency
* Data readability
* Time-based analysis
* Campaign categorization
* Customer journey analysis
* Dashboard readiness
* Reproducibility

Without these transformations, it would be more difficult to perform consistent analysis across channels, campaigns, and time periods.

---

# 25. Conclusion

The data cleaning process transformed the original Multi-Touch Marketing Attribution dataset into a structured dataset suitable for analysis.

The original dataset contained 10,000 rows and 5 columns. The `Timestamp` column was converted to datetime format, campaign placeholder values were standardized, additional date and time features were created, and a `Touchpoint_Order` column was added.

The final cleaned dataset contains:

```text
10,000 rows
11 columns
```

The final dataset contains no missing values in the required fields and is exported in both CSV and Excel formats.

The cleaned dataset provides the foundation for:

* SQL analysis
* KPI calculations
* Marketing attribution analysis
* Channel performance analysis
* Campaign performance analysis
* Customer journey analysis
* ROI analysis
* Dashboard development
* Business insights

This structured and reproducible cleaning workflow helps maintain data integrity and ensures that downstream analysis is based on consistent and validated data.
