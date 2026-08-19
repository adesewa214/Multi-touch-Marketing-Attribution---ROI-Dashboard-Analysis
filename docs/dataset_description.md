# Dataset Description

## 1. Project Dataset Overview

The project uses a multi-touch marketing attribution dataset to analyze customer interactions with different marketing channels and campaigns and evaluate their impact on conversions, revenue, cost, profit, and marketing performance.

The dataset represents individual marketing touchpoints associated with users. Each row records an interaction between a user and a marketing channel at a specific point in time.

The cleaned dataset is used as the foundation for:

* Data analysis
* Marketing attribution analysis
* Campaign performance evaluation
* SQL analysis
* KPI calculation
* ROI and ROAS analysis
* Dashboard development
* Business recommendations

---

## 2. Dataset Source

The raw dataset is stored in the project repository at:

```text
data/raw/multi_touch_attribution_data.csv
```

The cleaned dataset is generated and stored in:

```text
data/cleaned/cleaned_multi_touch_attribution_data.csv
```

An Excel version of the cleaned dataset is also generated for easier inspection and analysis:

```text
data/cleaned/cleaned_multi_touch_attribution_data.xlsx
```

---

## 3. Raw Dataset Structure

The initial raw dataset contained:

* **Rows:** 10,000
* **Columns:** 5

The original columns were:

| Column     | Description                                                     |
| ---------- | --------------------------------------------------------------- |
| User ID    | Unique identifier associated with a user                        |
| Timestamp  | Date and time at which the marketing touchpoint occurred        |
| Channel    | Marketing channel through which the user interaction occurred   |
| Campaign   | Marketing campaign associated with the interaction              |
| Conversion | Indicates whether the interaction/user resulted in a conversion |

The raw dataset initially contained only basic touchpoint and conversion information. Additional time-based and analytical columns were created during the data-cleaning and preparation process.

---

## 4. Raw Dataset Columns

### 4.1 User ID

**Column:** `User ID`

This column identifies the user associated with each marketing touchpoint.

A single user can appear multiple times because a user may interact with multiple marketing channels before converting or completing the customer journey.

The `User ID` column is therefore useful for:

* Identifying individual users
* Grouping touchpoints by user
* Understanding customer journeys
* Performing multi-touch attribution analysis
* Counting unique customers

---

### 4.2 Timestamp

**Column:** `Timestamp`

The `Timestamp` column records the date and time at which a marketing interaction occurred.

Initially, the column was stored as text/string data.

During data cleaning, it was converted into a proper datetime data type to make time-based analysis possible.

The converted column can be used for:

* Date-based analysis
* Monthly trends
* Daily trends
* Hourly trends
* Campaign timing analysis
* Channel performance over time

---

### 4.3 Channel

**Column:** `Channel`

The `Channel` column identifies the marketing channel associated with each touchpoint.

The dataset contains the following marketing channels:

* Email
* Search Ads
* Social Media
* Direct Traffic
* Referral
* Display Ads

These channels can be compared to determine which sources generate stronger engagement and conversions.

Channel-level analysis can support decisions related to:

* Marketing budget allocation
* Campaign optimization
* Customer acquisition
* Conversion performance
* ROI analysis

---

### 4.4 Campaign

**Column:** `Campaign`

The `Campaign` column identifies the marketing campaign associated with each touchpoint.

The original dataset contained the following campaign values:

* New Product Launch
* Winter Sale
* Brand Awareness
* Retargeting
* Discount Offer
* `-`

The `-` value represented interactions where no specific campaign was associated with the touchpoint.

During cleaning, these values were standardized to:

```text
No Campaign
```

Therefore, the final campaign categories are:

* New Product Launch
* Winter Sale
* Brand Awareness
* Retargeting
* Discount Offer
* No Campaign

Replacing the placeholder value with a meaningful category makes the dataset easier to understand and analyze.

---

### 4.5 Conversion

**Column:** `Conversion`

The `Conversion` column indicates whether the associated interaction resulted in a conversion.

The original dataset contained two values:

* `Yes`
* `No`

These values were retained during cleaning because they provide a direct indicator of conversion behavior.

The column can be used to calculate:

* Total conversions
* Conversion rate
* Channel conversion performance
* Campaign conversion performance
* Customer conversion behavior

---

## 5. Data Cleaning and Preparation

The raw dataset was reviewed and prepared before performing analysis.

The main objectives of the cleaning process were:

* Validate the dataset structure
* Inspect column names
* Check data types
* Identify missing values
* Standardize campaign values
* Convert timestamps into datetime format
* Create useful time-based columns
* Create touchpoint ordering information
* Export the cleaned dataset

---

## 6. Timestamp Conversion

The original `Timestamp` column was stored as text.

It was converted to a datetime data type during the cleaning process.

### Before cleaning

```text
Timestamp → string/object
```

### After cleaning

```text
Timestamp → datetime
```

This conversion allows the project to perform chronological and time-based analysis correctly.

---

## 7. Derived Date and Time Columns

Additional columns were created from the cleaned `Timestamp` column.

The following columns were added:

| Column | Description                               |
| ------ | ----------------------------------------- |
| Date   | Extracted calendar date from Timestamp    |
| Year   | Extracted year from Timestamp             |
| Month  | Extracted month from Timestamp            |
| Day    | Extracted day of the month from Timestamp |
| Hour   | Extracted hour from Timestamp             |

These columns simplify analysis without requiring the timestamp to be repeatedly transformed during queries or dashboard calculations.

### Example

If a timestamp contains:

```text
2025-02-15 14:30:00
```

The derived values can be represented as:

```text
Date  → 2025-02-15
Year  → 2025
Month → February
Day   → 15
Hour  → 14
```

---

## 8. Campaign Value Standardization

The raw dataset used the value:

```text
-
```

for interactions where a specific campaign was not available.

The number of such records was inspected by marketing channel.

The observed counts were:

| Channel        | `-` Campaign Records |
| -------------- | -------------------: |
| Direct Traffic |                1,721 |
| Email          |                  303 |
| Social Media   |                  285 |
| Display Ads    |                  281 |
| Referral       |                  277 |
| Search Ads     |                  264 |

Instead of treating `-` as an actual campaign name, the value was replaced with:

```text
No Campaign
```

This provides a more meaningful representation of the underlying data.

### Final Campaign Categories

After cleaning, the campaign column contains:

```text
Discount Offer
No Campaign
New Product Launch
Brand Awareness
Retargeting
Winter Sale
```

---

## 9. Touchpoint Order

A `Touchpoint_Order` column was added to support multi-touch customer journey analysis.

This column provides an ordering mechanism for touchpoints associated with users.

The ordering is useful for understanding the sequence in which users interact with marketing channels.

For example, a customer journey may contain:

```text
Email → Social Media → Search Ads → Conversion
```

The touchpoint order can help identify:

* First-touch interactions
* Later-stage interactions
* Customer journey sequences
* Number of touchpoints before conversion
* Potential attribution contributions

---

## 10. Missing Value Validation

Missing values were checked after the cleaning process.

The final cleaned dataset contained no missing values in the required columns.

| Column           | Missing Values After Cleaning |
| ---------------- | ----------------------------: |
| User ID          |                             0 |
| Timestamp        |                             0 |
| Channel          |                             0 |
| Campaign         |                             0 |
| Conversion       |                             0 |
| Touchpoint_Order |                             0 |
| Date             |                             0 |
| Year             |                             0 |
| Month            |                             0 |
| Day              |                             0 |
| Hour             |                             0 |

This validation confirms that the cleaned dataset is complete for the fields used in the project's analysis.

---

## 11. Final Cleaned Dataset Structure

After data preparation, the dataset contained:

* **Rows:** 10,000
* **Columns:** 11

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

### Final Dataset Schema

| Column           | Data Role                  | Description                            |
| ---------------- | -------------------------- | -------------------------------------- |
| User ID          | Identifier                 | Identifies the user                    |
| Timestamp        | Datetime                   | Date and time of the touchpoint        |
| Channel          | Categorical                | Marketing channel                      |
| Campaign         | Categorical                | Marketing campaign                     |
| Conversion       | Categorical                | Conversion status                      |
| Touchpoint_Order | Numeric                    | Order of the touchpoint                |
| Date             | Date                       | Calendar date extracted from Timestamp |
| Year             | Numeric                    | Year extracted from Timestamp          |
| Month            | Categorical/Date component | Month extracted from Timestamp         |
| Day              | Numeric                    | Day of month extracted from Timestamp  |
| Hour             | Numeric                    | Hour extracted from Timestamp          |

---

## 12. Final Data Types

The cleaned dataset uses appropriate data types for analysis.

The important type conversions include:

| Column           | Final Data Type     |
| ---------------- | ------------------- |
| User ID          | Identifier/Text     |
| Timestamp        | Datetime            |
| Channel          | Text/Categorical    |
| Campaign         | Text/Categorical    |
| Conversion       | Text/Categorical    |
| Touchpoint_Order | Integer             |
| Date             | Date                |
| Year             | Integer             |
| Month            | Date/Time component |
| Day              | Integer             |
| Hour             | Integer             |

The exact representation of some date-related columns may depend on the pandas/export format used when generating the cleaned CSV or Excel file.

---

## 13. Marketing Channels

The dataset contains six marketing channels:

### Email

Email represents marketing interactions delivered through email campaigns.

It can be analyzed to determine:

* Conversion performance
* Customer engagement
* Campaign effectiveness
* Contribution to customer journeys

### Search Ads

Search Ads represent interactions generated through paid search advertising.

They can be evaluated based on:

* Conversions
* Campaign performance
* Customer acquisition
* ROI and ROAS

### Social Media

Social Media represents interactions generated through social platforms.

It can be analyzed for:

* Engagement
* Conversion contribution
* Campaign effectiveness
* Customer journey influence

### Direct Traffic

Direct Traffic represents visits where users arrive directly rather than through an identified external marketing source.

This channel is particularly relevant when studying returning users and direct customer interactions.

### Referral

Referral represents traffic or interactions generated through referral sources.

It can be analyzed to understand the contribution of referral-based customer acquisition.

### Display Ads

Display Ads represent interactions generated through display advertising campaigns.

Their performance can be compared against other paid and organic channels.

---

## 14. Marketing Campaigns

The final dataset contains six campaign categories.

| Campaign           | Description                                                          |
| ------------------ | -------------------------------------------------------------------- |
| New Product Launch | Campaign associated with promoting a new product                     |
| Winter Sale        | Seasonal promotional campaign                                        |
| Brand Awareness    | Campaign focused on increasing brand visibility                      |
| Retargeting        | Campaign targeting users who previously interacted with the business |
| Discount Offer     | Promotional campaign using discounts or special offers               |
| No Campaign        | Touchpoint not associated with a specific campaign                   |

Campaign-level analysis can help determine which campaigns are associated with higher conversion and marketing performance.

---

## 15. Conversion Values

The `Conversion` field contains two categories:

| Value | Meaning                                                  |
| ----- | -------------------------------------------------------- |
| Yes   | The associated interaction/user resulted in a conversion |
| No    | No conversion was recorded                               |

Conversion information is used as one of the primary measures of marketing effectiveness.

---

## 16. Data Quality Checks

The following checks were performed as part of the data preparation process:

### Dataset Shape

The initial dataset was verified to contain:

```text
10,000 rows
5 columns
```

### Column Validation

The expected raw columns were verified:

```text
User ID
Timestamp
Channel
Campaign
Conversion
```

### Channel Validation

The available channel categories were inspected and verified.

### Campaign Validation

Campaign values were inspected and the placeholder `-` value was identified.

### Conversion Validation

Conversion values were checked to ensure that the expected categories were present:

```text
Yes
No
```

### Timestamp Validation

The timestamp field was converted from text to datetime.

### Missing Value Validation

Missing values were checked after cleaning and no missing values were present in the final required columns.

---

## 17. Data Transformation Summary

The major transformations performed during data preparation are summarized below:

| Step | Transformation                        |
| ---- | ------------------------------------- |
| 1    | Loaded the raw CSV dataset            |
| 2    | Inspected dataset shape and structure |
| 3    | Reviewed column names and values      |
| 4    | Converted `Timestamp` to datetime     |
| 5    | Created `Date` column                 |
| 6    | Created `Year` column                 |
| 7    | Created `Month` column                |
| 8    | Created `Day` column                  |
| 9    | Created `Hour` column                 |
| 10   | Identified `-` campaign values        |
| 11   | Replaced `-` with `No Campaign`       |
| 12   | Added `Touchpoint_Order`              |
| 13   | Validated missing values              |
| 14   | Verified final dataset structure      |
| 15   | Exported cleaned CSV                  |
| 16   | Exported cleaned Excel file           |

---

## 18. Cleaned Dataset Output

The cleaned dataset is generated in the following locations:

### CSV

```text
data/cleaned/cleaned_multi_touch_attribution_data.csv
```

### Excel

```text
data/cleaned/cleaned_multi_touch_attribution_data.xlsx
```

The CSV file is intended for programmatic analysis and downstream processing, while the Excel file provides a convenient format for manual inspection and review.

---

## 19. Dataset Usage in the Project

The cleaned dataset serves as the foundation for the project's analytical workflow.

It is used for:

### Marketing Attribution

Analyzing how different marketing touchpoints contribute to conversions.

### Campaign Analysis

Comparing campaigns based on conversion and marketing performance.

### Channel Analysis

Evaluating the relative contribution of different marketing channels.

### Customer Journey Analysis

Examining the sequence of marketing touchpoints associated with users.

### SQL Analysis

The cleaned data structure is used as the basis for SQL queries and KPI calculations.

### Dashboard Development

The prepared dataset provides structured fields required for dashboard visualizations and interactive analysis.

---

## 20. Relationship Between Raw and Cleaned Data

The data pipeline can be represented as:

```text
Raw Dataset
    ↓
Data Inspection
    ↓
Data Type Validation
    ↓
Timestamp Conversion
    ↓
Date/Time Feature Creation
    ↓
Campaign Value Standardization
    ↓
Touchpoint Ordering
    ↓
Missing Value Validation
    ↓
Cleaned Dataset
    ↓
SQL Analysis
    ↓
KPI Analysis
    ↓
Dashboard
```

This process ensures that the data is prepared consistently before analysis and visualization.

---

## 21. Data Cleaning Files

The cleaning process is implemented through the project's Python data-cleaning script.

The script is located at:

```text
scripts/data_cleaning.py
```

The script performs the required transformations and exports the cleaned dataset.

This makes the cleaning process reproducible and allows the same transformations to be applied again if the raw dataset is updated.

---

## 22. Reproducibility

The project follows a reproducible data-processing workflow.

To reproduce the cleaned dataset:

1. Place the raw dataset in:

```text
data/raw/multi_touch_attribution_data.csv
```

2. Run the cleaning script:

```bash
python scripts/data_cleaning.py
```

3. The cleaned CSV and Excel files will be generated in:

```text
data/cleaned/
```

This approach keeps the raw data unchanged while creating separate processed outputs.

---

## 23. Data Folder Structure

The project follows the following basic data organization:

```text
data/
├── raw/
│   └── multi_touch_attribution_data.csv
│
└── cleaned/
    ├── cleaned_multi_touch_attribution_data.csv
    └── cleaned_multi_touch_attribution_data.xlsx
```

The separation between raw and cleaned data helps preserve the original dataset and prevents accidental modification of source data.

---

## 24. Data Governance and Integrity

The raw dataset is preserved separately from the cleaned dataset.

The cleaning process does not overwrite the original raw file.

Instead:

* Raw data is retained in `data/raw/`
* Processed data is stored in `data/cleaned/`
* Transformations are implemented through Python
* Data quality checks are performed after cleaning
* The cleaned output is used for subsequent analysis

This structure improves traceability and reproducibility throughout the project.

---

## 25. Summary

The Multi-Touch Marketing Attribution dataset contains user-level marketing touchpoint information used to analyze customer interactions, conversions, channels, and campaigns.

The original dataset contained 10,000 records and 5 columns. During the data-cleaning stage, the timestamp field was converted into a datetime format, additional date and time features were created, campaign placeholders were standardized, and touchpoint ordering was added.

The resulting cleaned dataset contains 10,000 records and 11 columns with no missing values in the required fields.

The cleaned dataset provides a structured foundation for:

* Multi-touch attribution analysis
* Marketing channel analysis
* Campaign performance analysis
* Conversion analysis
* SQL queries
* KPI calculations
* ROI and ROAS analysis
* Dashboard visualization
* Business recommendations

The cleaned data is maintained separately from the raw data to support reproducibility, data integrity, and a clear analytical workflow.
