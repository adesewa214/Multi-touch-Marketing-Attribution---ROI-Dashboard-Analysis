# Dataset Description

## 1. Project Dataset Overview

The project uses a multi-touch marketing attribution dataset to analyze customer interactions with different marketing channels and campaigns and evaluate their impact on conversions, revenue, cost, profit, and marketing performance.

The dataset represents individual marketing touchpoints associated with users. Each record contains information about the user, the time of interaction, the marketing channel and campaign involved, conversion status, and financial performance metrics.

The dataset is used as the foundation for SQL analysis, dashboard development, ROI analysis, and multi-touch marketing attribution.

---

## 2. Dataset Source

**Dataset File:**

`final_multi_touch_attribution_roi_dataset_v2.csv`

The dataset is stored in the project's raw data directory:

```text
data/raw/

---

## 3. Dataset Size

The dataset contains **10,000 records** and initially contains **13 columns**.

During the data cleaning process, an additional `Touchpoint_Order` column was created to identify the chronological order of marketing interactions for each user.

Therefore, the final cleaned dataset contains **10,000 records and 14 columns**.

### Dataset Statistics

| Metric | Value |
|---|---:|
| Initial Records | 10,000 |
| Final Records | 10,000 |
| Initial Columns | 13 |
| Final Columns | 14 |
| Duplicate Records Removed | 0 |
| Missing CPA Values | 5,056 |
| Missing Values After Cleaning | 0 |
| Unique Users | 2,847 |
| Unique Channels | 6 |
| Unique Campaigns | 6 |
| Total Conversions | 4,944 |
| Total Touchpoints | 10,000 |

---

## 4. Dataset Columns

The dataset contains the following fields:

| Column | Description | Data Type |
|---|---|---|
| User ID | Unique identifier of the user/customer | Integer |
| Timestamp | Date and time of the marketing interaction | Datetime |
| Channel | Marketing channel through which the interaction occurred | String |
| Campaign | Marketing campaign associated with the interaction | String |
| Conversion | Indicates whether the interaction resulted in a conversion | Integer (0/1) |
| Campaign_Cost_USD | Cost associated with the marketing campaign | Float |
| Budget_USD | Budget allocated to the campaign | Float |
| Revenue_USD | Revenue generated from the interaction/conversion | Float |
| Profit_USD | Profit generated after subtracting campaign cost from revenue | Float |
| ROI_% | Return on Investment expressed as a percentage | Float |
| ROAS | Return on Ad Spend | Float |
| CPA_USD | Cost per Acquisition | Float |
| Performance_Rating | Overall performance classification of the interaction/campaign | String |
| Touchpoint_Order | Sequential order of each user's marketing interaction | Integer |

---

## 5. Marketing Channels

The dataset contains six marketing channels:

- Email
- Search Ads
- Social Media
- Direct Traffic
- Referral
- Display Ads

The cleaned dataset contains the following distribution:

| Channel | Touchpoints |
|---|---:|
| Direct Traffic | 1,721 |
| Referral | 1,685 |
| Display Ads | 1,669 |
| Social Media | 1,662 |
| Email | 1,654 |
| Search Ads | 1,609 |

These channels are used to compare marketing performance and identify which channels generate better conversion and financial results.

---

## 6. Campaign Information

The dataset contains the following campaign categories:

- New Product Launch
- Winter Sale
- Brand Awareness
- Retargeting
- Discount Offer
- No Campaign

Records containing `-` in the Campaign column were standardized to **No Campaign** during data cleaning.

This ensures that missing or unavailable campaign information is represented consistently.

---

## 7. Conversion Information

The original `Conversion` column contained two values:

- `Yes`
- `No`

During data cleaning, these values were converted into binary values:

| Original Value | Cleaned Value |
|---|---:|
| Yes | 1 |
| No | 0 |

This conversion makes the field easier to use in SQL queries, statistical analysis, KPI calculations, and dashboard visualizations.

The cleaned dataset contains:

- **4,944 successful conversions**
- **5,056 non-conversions**

---

## 8. Financial Metrics

The dataset contains several financial performance measures.

### Campaign Cost

`Campaign_Cost_USD` represents the amount spent on a marketing campaign.

### Budget

`Budget_USD` represents the allocated marketing budget.

### Revenue

`Revenue_USD` represents the revenue generated.

### Profit

`Profit_USD` represents the amount remaining after campaign cost is deducted from revenue.

The cleaning process recalculates Profit using:

```text
Profit = Revenue - Campaign Cost