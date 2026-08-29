# SQL Logic Documentation

## 1. Overview

This document explains the SQL analysis performed for the **Multi-Touch Marketing Attribution & ROI Dashboard** project.

The SQL analysis is performed using the marketing attribution data stored in the SQL Server database table:

```text
dbo.Multi_touch_market_attribution
```

The purpose of the SQL analysis is to transform the marketing attribution data into meaningful business metrics that can be used to evaluate customer behavior, marketing performance, campaign effectiveness, channel performance, revenue, cost, profit, ROI, conversions, and customer journeys.

The SQL analysis also provides supporting metrics for the project dashboard and helps generate data-driven business insights and recommendations.

---

## 2. SQL Analysis Objectives

The main objectives of the SQL analysis are:

* Calculate overall marketing KPIs.
* Measure the total number of customers.
* Measure total marketing touchpoints.
* Measure total conversions.
* Calculate overall conversion rate.
* Calculate total revenue.
* Calculate total campaign cost.
* Calculate total marketing budget.
* Calculate total profit.
* Calculate average CPA.
* Compare CPA across campaigns.
* Compare CPA across marketing channels.
* Calculate average ROI.
* Compare ROI across marketing channels.
* Analyze revenue by campaign and marketing channel.
* Analyze profit by campaign and marketing channel.
* Analyze budget allocation by campaign.
* Analyze campaign cost by campaign.
* Analyze conversion rates by campaign and channel.
* Analyze conversions by campaign, channel, and touchpoint order.
* Analyze customer journey length.
* Identify customers with the longest conversion journeys.
* Calculate average customer journey length.
* Calculate average time to conversion.
* Identify common customer journeys.
* Analyze first-touch and last-touch attribution.
* Analyze monthly conversion trends.
* Analyze monthly revenue trends.
* Analyze monthly revenue by marketing channel.
* Analyze performance ratings by campaign and marketing channel.
* Analyze touchpoint-order distribution.
* Analyze touchpoints by marketing channel.

---

## 3. Data Source

The SQL analysis uses the following SQL Server table:

```text
dbo.Multi_touch_market_attribution
```

The table contains the marketing attribution records used throughout the SQL analysis.

### Main Columns Used

| Column               | Purpose                                                     |
| -------------------- | ----------------------------------------------------------- |
| `User_ID`            | Identifies an individual customer/user                      |
| `Timestamp`          | Date and time of a marketing interaction                    |
| `Channel`            | Marketing channel associated with a touchpoint              |
| `Campaign`           | Marketing campaign associated with the touchpoint           |
| `Conversion`         | Indicates whether the record represents a conversion        |
| `Touchpoint_Order`   | Indicates the order of a touchpoint in the customer journey |
| `CPA_USD`            | Customer acquisition cost                                   |
| `ROI`                | Return on investment                                        |
| `Revenue_USD`        | Revenue generated                                           |
| `Profit_USD`         | Profit generated                                            |
| `Campaign_Cost_USD`  | Cost associated with the campaign                           |
| `Budget_USD`         | Marketing budget                                            |
| `Performance_Rating` | Marketing performance rating                                |
| `Touchpoints`        | Number of customer touchpoints where applicable             |
| `Days_To_Convert`    | Number of days taken to convert where applicable            |

---

## 4. SQL Analysis Workflow

The SQL analysis follows the overall project workflow:

```text
Raw Marketing Attribution Dataset
              ↓
        Data Cleaning
              ↓
       Cleaned Dataset
              ↓
      SQL Database Table
              ↓
         SQL Queries
              ↓
       KPI Calculations
              ↓
      Dashboard Analysis
              ↓
      Business Insights
              ↓
 Business Recommendations
```

### Step 1: Data Cleaning

The raw marketing attribution dataset is cleaned before the SQL analysis is performed.

The cleaning process prepares the dataset for analysis by checking data quality, standardizing values, handling invalid values, and preparing appropriate fields.

### Step 2: Load Data into SQL

The cleaned data is stored in the SQL Server table:

```text
dbo.Multi_touch_market_attribution
```

### Step 3: Execute SQL Queries

Individual SQL queries are used to calculate overall KPIs, campaign-level metrics, channel-level metrics, customer journey metrics, attribution metrics, and time-based trends.

### Step 4: Analyze Results

The query results are used to understand marketing performance and customer behavior.

### Step 5: Support Dashboard Development

The calculated SQL metrics can be used as supporting values for dashboard KPI cards, charts, tables, and other visualizations.

---

# 5. SQL Queries and Logic

## 5.1 Average CPA

### Query File

`Average_CPA.sql`

### Purpose

Calculates the overall average Customer Acquisition Cost (CPA).

### Logic

The query calculates the average value of `CPA_USD` across all records and rounds the result to two decimal places.

### Formula

```text
Average CPA = AVG(CPA_USD)
```

### Business Interpretation

Average CPA represents the average cost associated with customer acquisition.

A lower CPA generally indicates more cost-efficient customer acquisition.

---

## 5.2 Average CPA by Campaign

### Query File

`Average_CPA_by_Campaign.sql`

### Purpose

Calculates the average CPA for each marketing campaign.

### Logic

The data is grouped by `Campaign`. The average `CPA_USD` is calculated for each campaign and rounded to two decimal places.

The results are sorted in ascending order of average CPA.

### Key SQL Logic

```text
GROUP BY Campaign
ORDER BY Average_CPA ASC
```

### Business Interpretation

This query allows campaigns to be compared based on customer acquisition efficiency.

Campaigns appearing at the top of the result have lower average CPA.

---

## 5.3 Average CPA by Marketing Channel

### Query File

`Average_CPA_by_Marketing_Channel.sql`

### Purpose

Calculates average CPA for each marketing channel.

### Logic

The records are grouped by `Channel`, and the average `CPA_USD` is calculated.

The results are rounded to two decimal places and sorted by average CPA in ascending order.

### Key SQL Logic

```text
GROUP BY Channel
ORDER BY Average_CPA ASC
```

### Business Interpretation

This query helps identify marketing channels that acquire customers at relatively lower or higher costs.

---

## 5.4 Average Customer Journey Length

### Query File

`Average_Customer_Journey_Length.sql`

### Purpose

Calculates the average number of touchpoints in a customer's journey.

### Logic

The inner query groups records by `User_ID` and counts the number of records for each user.

```text
COUNT(*) AS Touchpoints
```

The outer query calculates the average number of touchpoints across customers.

The touchpoint count is converted to `FLOAT` before calculating the average and the final value is rounded to two decimal places.

### Calculation

```text
Touchpoints per Customer = COUNT(*) grouped by User_ID

Average Journey Length = AVG(Touchpoints)
```

### Business Interpretation

This metric indicates the average number of marketing interactions recorded for a customer.

A higher value indicates that customers generally interact with more marketing touchpoints during their recorded journey.

---

## 5.5 Average Profit per Customer

### Query File

`Average_Profit_per_customer.sql`

### Purpose

Calculates the average profit generated per unique customer.

### Logic

The query calculates total profit using `SUM(Profit_USD)` and divides it by the number of unique customers using `COUNT(DISTINCT User_ID)`.

### Formula

```text
Profit Per Customer =
SUM(Profit_USD) / COUNT(DISTINCT User_ID)
```

The result is rounded to two decimal places.

### Business Interpretation

This metric represents the average profit generated by each unique customer.

A higher profit per customer generally indicates stronger customer profitability.

---

## 5.6 Average ROI

### Query File

`Average_ROI.sql`

### Purpose

Calculates the overall average Return on Investment.

### Logic

The query calculates:

```text
AVG(ROI)
```

and rounds the result to two decimal places.

### Business Interpretation

Average ROI provides an overall indication of marketing investment efficiency.

Higher ROI generally indicates stronger returns relative to investment.

---

## 5.7 Average ROI by Campaign

### Query File

`Average_ROI_by_Campaign.sql`

### Status

The file is currently empty and does not contain an implemented SQL query.

Therefore, no campaign-level ROI calculation is currently included in the SQL analysis.

### Status

```text
Pending SQL implementation
```

No result should be reported for this metric until the SQL query is implemented.

---

## 5.8 Average ROI by Marketing Channel

### Query File

`Average_ROI_by_Marketing_Channel.sql`

### Purpose

Calculates average ROI for each marketing channel.

### Logic

The records are grouped by `Channel`.

The average `ROI` is calculated for each channel, rounded to two decimal places, and sorted in descending order.

### Key SQL Logic

```text
GROUP BY Channel
ORDER BY Average_ROI DESC
```

### Business Interpretation

This query helps identify marketing channels that generate stronger returns relative to investment.

Channels with higher average ROI appear first.

---

## 5.9 Average Time to Conversion

### Query File

`Average_Time_to_Conversion.sql`

### Purpose

Calculates the average number of days between the earliest and latest recorded marketing interaction for converted users.

### Logic

Only converted records are considered:

```text
WHERE Conversion = 1
```

For each user, the query finds:

```text
MIN([Timestamp])
```

and:

```text
MAX([Timestamp])
```

The difference between the two timestamps is calculated using:

```text
DATEDIFF(DAY, MIN([Timestamp]), MAX([Timestamp]))
```

The resulting value is called `Days_To_Convert`.

The outer query calculates the average number of days.

### Calculation

```text
Days To Convert =
Latest Timestamp - Earliest Timestamp
```

```text
Average Days =
AVG(Days_To_Convert)
```

### Business Interpretation

Average time to conversion indicates the typical duration of the recorded customer journey for converted users.

---

## 5.10 Average Revenue per Customer

### Query File

`Average_revnue_per_customer.sql`

### Purpose

Calculates average revenue generated per unique customer.

### Logic

Total revenue is calculated using:

```text
SUM(Revenue_USD)
```

Unique customers are calculated using:

```text
COUNT(DISTINCT User_ID)
```

The two values are divided and rounded to two decimal places.

### Formula

```text
Revenue Per Customer =
SUM(Revenue_USD) / COUNT(DISTINCT User_ID)
```

### Business Interpretation

Revenue per customer represents the average revenue generated by each unique customer.

---

# 6. Budget and Cost Analysis

## 6.1 Budget Allocation by Campaign

### Query File

`Budget_Allocation_by_Campaign.sql`

### Purpose

Calculates the total marketing budget allocated to each campaign.

### Logic

The query groups records by `Campaign` and calculates:

```text
SUM(Budget_USD)
```

The result is rounded to two decimal places and sorted in descending order.

### Key SQL Logic

```text
GROUP BY Campaign
ORDER BY Total_Budget DESC
```

### Business Interpretation

This query helps identify which campaigns receive the largest marketing budgets.

---

## 6.2 Campaign Cost by Campaign

### Query File

`Campaign_Cost_by_Campaign.sql`

### Purpose

Calculates the total campaign cost for each marketing campaign.

### Logic

The query groups records by `Campaign` and calculates:

```text
SUM(Campaign_Cost_USD)
```

The results are rounded to two decimal places and sorted in descending order.

### Business Interpretation

This metric helps compare campaign spending and identify campaigns with higher marketing costs.

---

# 7. Conversion Analysis

## 7.1 Conversion Rate by Campaign

### Query File

`Conversion_Rate_by_Campaign.sql`

### Purpose

Calculates the conversion rate for each campaign.

### Logic

The query counts records where:

```text
Conversion = 1
```

and divides the number of conversions by the total number of records.

The result is multiplied by 100 to obtain a percentage and rounded to two decimal places.

### Formula

```text
Conversion Rate =
(Conversions / Total Records) × 100
```

### Business Interpretation

This metric allows campaigns to be compared based on their conversion performance.

---

## 7.2 Conversion Rate by Marketing Channel

### Query File

`Conversion_Rate_by_Marketing_Channel.sql`

### Purpose

Calculates the conversion rate for each marketing channel.

### Logic

The records are grouped by `Channel`.

The query counts converted records using:

```text
COUNT(CASE WHEN Conversion = 1 THEN 1 END)
```

and divides this by the total number of records in each channel.

The result is multiplied by 100 and rounded to two decimal places.

### Business Interpretation

This metric helps identify channels with stronger or weaker conversion performance.

---

## 7.3 Conversions by Marketing Channel

### Query File

`Conversion_by_Marketing_Chanel.sql`

### Purpose

Calculates the total number of conversions generated by each marketing channel.

### Logic

Only converted records are selected:

```text
WHERE Conversion = 1
```

The records are grouped by `Channel` and counted.

### Key SQL Logic

```text
GROUP BY Channel
ORDER BY Total_Conversions DESC
```

### Business Interpretation

This query identifies the channels that contribute the highest number of conversions.

---

## 7.4 Conversions by Campaign

### Query File

`Conversions_by_Campaign.sql`

### Purpose

Calculates the total number of conversions generated by each campaign.

### Logic

Only records where `Conversion = 1` are included.

The results are grouped by `Campaign` and sorted by total conversions in descending order.

### Business Interpretation

This allows campaigns to be compared based on the number of conversions they generate.

---

## 7.5 Conversions by Touchpoint Order

### Query File

`conversions_by_Touchpoint_Order.sql`

### Purpose

Analyzes the number of conversions associated with each touchpoint order.

### Logic

Converted records are filtered using:

```text
WHERE Conversion = 1
```

The results are grouped by `Touchpoint_Order`.

### Business Interpretation

This analysis helps understand how conversions are distributed across different positions in the customer journey.

---

## 7.6 Overall Conversion Rate

### Query File

`Overall_Conversion_Rate.sql`

### Purpose

Calculates overall conversion metrics for the complete dataset.

### Query Components

The file contains two calculations.

#### Total Conversions

The first query counts records where:

```text
Conversion = 1
```

This produces:

```text
Total_Conversions
```

#### Conversion Rate Percentage

The second query calculates:

```text
Conversion Rate =
(Conversions / Total Records) × 100
```

The result is returned as:

```text
Conversion_Rate_Percentage
```

and converted to a decimal value with two decimal places.

### Business Interpretation

These metrics provide a high-level view of overall conversion performance.

---

## 7.7 Total Conversions

### Query File

`Total_conversions.sql`

### Purpose

Calculates the total number of conversions in the dataset.

### Logic

The query filters records where:

```text
Conversion = 1
```

and counts the resulting records.

### Output

```text
Total_Conversions
```

---

# 8. Customer Journey Analysis

## 8.1 Customer Journey Length by User

### Query File

`Customer_Journey_Length_by_User.sql`

### Purpose

Calculates the total number of touchpoints for each customer.

### Logic

The records are grouped by `User_ID` and counted.

### Formula

```text
Total Touchpoints per User = COUNT(*)
```

### Sorting

Customers are sorted by total touchpoints in descending order.

### Business Interpretation

This identifies customers with shorter or longer recorded marketing journeys.

---

## 8.2 Customers with Longest Conversion Journey

### Query File

`Customers_Longest_Conversion_Journey.sql`

### Purpose

Identifies the top 10 customers with the highest number of touchpoints associated with conversion.

### Logic

The query:

* Selects the top 10 users.
* Filters records where `Conversion = 1`.
* Groups records by `User_ID`.
* Counts touchpoints.
* Sorts by total touchpoints in descending order.

### Business Interpretation

This helps identify customers whose conversion journeys involved a larger number of recorded marketing touchpoints.

---

## 8.3 Customers with Longest Conversion Time

### Query File

`Customers_Longest_Conversion_Time.sql`

### Purpose

Identifies the top 10 customers with the longest recorded conversion time.

### Logic

Only converted records are included.

For each user, the query calculates the number of days between the earliest and latest timestamps.

```text
DATEDIFF(
    DAY,
    MIN([Timestamp]),
    MAX([Timestamp])
)
```

The results are sorted by `Days_To_Convert` in descending order.

### Business Interpretation

This identifies customers who took the longest recorded time to convert.

---

## 8.4 Most Common Customer Journey

### Query File

`Most_Common_Customer_Journey.sql`

### Purpose

Identifies the most frequently occurring sequence of marketing channels in customer journeys.

### Logic

For each user, the query uses:

```text
STRING_AGG(Channel, ' → ')
```

to combine marketing channels into a journey sequence.

The channels are ordered using:

```text
WITHIN GROUP (ORDER BY Touchpoint_Order)
```

The resulting journey is then grouped and counted.

### Output

The query returns:

* `Journey`
* `Frequency`

### Business Interpretation

This analysis identifies common paths customers follow across marketing channels.

It can help the team understand frequently occurring channel sequences in the customer journey.

---

# 9. Attribution Analysis

## 9.1 First-Touch Attribution by Campaign

### Query File

`First-Touch_Attribution_by_Campaign.sql`

### Purpose

Measures the number of first-touch interactions attributed to each campaign.

### Logic

The first touchpoint is identified using:

```text
Touchpoint_Order = 1
```

The records are grouped by `Campaign` and counted.

### Business Interpretation

This shows which campaigns most frequently appear as the first recorded marketing interaction in customer journeys.

---

## 9.2 First-Touch Attribution by Channel

### Query File

`First-Touch_Attribution_by_Channel.sql`

### Purpose

Measures the number of first-touch interactions attributed to each marketing channel.

### Logic

Records where:

```text
Touchpoint_Order = 1
```

are selected.

The results are grouped by `Channel` and counted.

### Business Interpretation

This identifies channels that most frequently initiate customer journeys.

---

## 9.3 Last-Touch Attribution by Campaign

### Query File

`Last-Touch_Attribution_by_Campaign.sql`

### Purpose

Measures the number of last-touch interactions attributed to each campaign.

### Logic

A Common Table Expression named `LastTouch` is used.

The query applies:

```text
ROW_NUMBER() OVER (
    PARTITION BY User_ID
    ORDER BY Touchpoint_Order DESC
)
```

This assigns row number 1 to the last touchpoint for each user.

Only:

```text
rn = 1
```

is retained.

The results are grouped by `Campaign`.

### Business Interpretation

This identifies campaigns that most frequently appear as the final recorded marketing interaction before the end of a customer journey.

---

## 9.4 Last-Touch Attribution by Channel

### Query File

`Last-Touch_Attribution_by_Channel.sql`

### Purpose

Measures the number of last-touch interactions attributed to each marketing channel.

### Logic

The query uses `ROW_NUMBER()` partitioned by `User_ID` and ordered by `Touchpoint_Order DESC`.

The final touchpoint for each user is identified using:

```text
rn = 1
```

The results are grouped by `Channel`.

### Business Interpretation

This identifies channels that most frequently occur as the final recorded touchpoint in customer journeys.

---

# 10. Revenue Analysis

## 10.1 Monthly Revenue Trend

### Query File

`Monthly_Revenue_Trend.sql`

### Purpose

Analyzes total revenue by month and year.

### Logic

The query extracts:

```text
YEAR([Timestamp])
MONTH([Timestamp])
```

and groups the records by year and month.

Total revenue is calculated using:

```text
SUM(Revenue_USD)
```

The result is rounded to two decimal places.

### Business Interpretation

This query helps identify changes and trends in revenue over time.

---

## 10.2 Monthly Revenue by Marketing Channel

### Query File

`Monthly_Revenue_by_Marketing_Channel.sql`

### Purpose

Analyzes monthly revenue separately for each marketing channel.

### Logic

The query groups records by:

* Year
* Month
* Channel

Revenue is calculated using:

```text
SUM(Revenue_USD)
```

### Business Interpretation

This allows the team to analyze revenue trends for individual marketing channels over time.

---

## 10.3 Revenue by Campaign

### Query File

`Revenue_by_Campaign.sql`

### Purpose

Calculates total revenue generated by each marketing campaign.

### Logic

The records are grouped by `Campaign`.

Total revenue is calculated using:

```text
SUM(Revenue_USD)
```

The results are rounded to two decimal places and sorted in descending order.

### Business Interpretation

This identifies campaigns generating higher or lower total revenue.

---

## 10.4 Revenue by Marketing Channel

### Query File

`Revenue_by_Marketing_Channel.sql`

### Purpose

Calculates total revenue generated by each marketing channel.

### Logic

The query groups records by `Channel` and calculates:

```text
SUM(Revenue_USD)
```

The results are rounded to two decimal places and sorted by total revenue in descending order.

### Business Interpretation

This allows comparison of revenue contribution across marketing channels.

---

## 10.5 Total Revenue

### Query File

`Total_Revenue.sql`

### Purpose

Calculates total revenue across the complete dataset.

### Formula

```text
Total Revenue = SUM(Revenue_USD)
```

The result is rounded to two decimal places.

---

# 11. Monthly Conversion Analysis

## 11.1 Monthly Conversion Trend

### Query File

`Monthly_Conversion_Trend.sql`

### Purpose

Analyzes the number of conversions by month and year.

### Logic

Only converted records are included.

The query extracts year and month from the timestamp and counts conversions.

### Business Interpretation

This helps identify increases, decreases, and patterns in conversion activity over time.

---

# 12. Performance Rating Analysis

## 12.1 Performance Rating by Campaign

### Query File

`Performance_Rating_by_Campaign.sql`

### Purpose

Analyzes the frequency of performance ratings within each campaign.

### Logic

The query groups records by:

* `Campaign`
* `Performance_Rating`

It then counts the number of records for each combination.

### Output

```text
Campaign
Performance_Rating
Frequency
```

### Business Interpretation

This helps understand the distribution of performance ratings across campaigns.

---

## 12.2 Performance Rating by Marketing Channel

### Query File

`Performance_Rating_by_Marketing_Channel.sql`

### Purpose

Analyzes the frequency of performance ratings within each marketing channel.

### Logic

The query groups records by:

* `Channel`
* `Performance_Rating`

and calculates the frequency of each rating.

### Business Interpretation

This helps evaluate how performance ratings are distributed across different marketing channels.

---

# 13. Profit Analysis

## 13.1 Profit by Campaign

### Query File

`Profit_by_Campaign.sql`

### Purpose

Calculates total profit generated by each marketing campaign.

### Logic

The query groups records by `Campaign` and calculates:

```text
SUM(Profit_USD)
```

The results are rounded to two decimal places and sorted in descending order.

### Business Interpretation

This identifies campaigns contributing the highest total profit.

---

## 13.2 Profit by Marketing Channel

### Query File

`Profit_by_Marketing_Channel.sql`

### Purpose

Calculates total profit generated by each marketing channel.

### Logic

The query groups records by `Channel` and calculates:

```text
SUM(Profit_USD)
```

The results are rounded to two decimal places and sorted in descending order.

### Business Interpretation

This helps identify channels contributing the highest total profit.

---

## 13.3 Total Profit

### Query File

`Total_profit.sql`

### Purpose

Calculates total profit across the dataset.

### Formula

```text
Total Profit = SUM(Profit_USD)
```

The result is rounded to two decimal places.

---

# 14. Customer and Touchpoint Metrics

## 14.1 Total Customers

### Query File

`Total_Customer.sql`

### Purpose

Calculates the total number of unique customers.

### Logic

The query uses:

```text
COUNT(DISTINCT User_ID)
```

### Output

```text
Total_Customers
```

### Business Interpretation

This represents the total unique customer population in the dataset.

---

## 14.2 Total Marketing Touchpoints

### Query File

`Total_marketing_touchpoints.sql`

### Purpose

Calculates the total number of marketing touchpoints.

### Logic

Each record is treated as a marketing touchpoint, so the query uses:

```text
COUNT(*)
```

### Output

```text
Total_Touchpoints
```

### Business Interpretation

This represents the overall volume of recorded marketing interactions.

---

## 14.3 Touchpoint Order Distribution

### Query File

`Touchpoint_order_distribution.sql`

### Purpose

Analyzes how frequently each touchpoint order occurs.

### Logic

Records are grouped by `Touchpoint_Order` and counted.

### Output

```text
Touchpoint_Order
Frequency
```

### Business Interpretation

This helps understand the distribution of touchpoint positions across customer journeys.

---

## 14.4 Touchpoints by Marketing Channel

### Query File

`Touchpoints_by_Marketing_Channel.sql`

### Purpose

Calculates the total number of marketing touchpoints associated with each channel.

### Logic

The records are grouped by `Channel` and counted.

### Business Interpretation

This identifies the marketing channels with the highest volume of customer interactions.

---

# 15. Budget and Overall Financial KPIs

## 15.1 Total Budget

### Query File

`Total_Budget.sql`

### Purpose

Calculates the total marketing budget.

### Formula

```text
Total Budget = SUM(Budget_USD)
```

The result is rounded to two decimal places.

---

## 15.2 Total Campaign Cost

### Query File

`Total_campaign_cost.sql`

### Purpose

Calculates the total campaign cost.

### Formula

```text
Total Campaign Cost = SUM(Campaign_Cost_USD)
```

The result is rounded to two decimal places.

---

# 16. SQL Functions and Techniques Used

The SQL analysis uses several SQL functions and techniques.

| SQL Function / Technique | Purpose                                |
| ------------------------ | -------------------------------------- |
| `AVG()`                  | Calculates averages                    |
| `SUM()`                  | Calculates totals                      |
| `COUNT()`                | Counts records                         |
| `COUNT(DISTINCT)`        | Counts unique customers                |
| `COUNT(CASE WHEN...)`    | Counts records meeting a condition     |
| `ROUND()`                | Rounds numerical results               |
| `GROUP BY`               | Groups records for aggregate analysis  |
| `ORDER BY`               | Sorts query results                    |
| `WHERE`                  | Filters records                        |
| `CASE WHEN`              | Applies conditional logic              |
| `CAST()`                 | Converts data types                    |
| `DATEDIFF()`             | Calculates date/time differences       |
| `MIN()`                  | Finds the earliest value               |
| `MAX()`                  | Finds the latest value                 |
| `YEAR()`                 | Extracts the year from a date          |
| `MONTH()`                | Extracts the month from a date         |
| `STRING_AGG()`           | Combines values into a single string   |
| `WITHIN GROUP`           | Controls ordering within aggregation   |
| `ROW_NUMBER()`           | Assigns sequential row numbers         |
| `PARTITION BY`           | Creates groups for window functions    |
| `TOP`                    | Limits the number of returned rows     |
| `WITH` / CTE             | Creates a temporary named query result |

---

# 17. Data Validation

The SQL analysis should be performed after the data-cleaning stage.

Important validation checks include:

* Checking for missing values.
* Checking for duplicate records.
* Verifying column names.
* Verifying data types.
* Checking conversion values.
* Checking campaign values.
* Checking marketing channel values.
* Checking timestamp values.
* Checking financial values.
* Checking customer identifiers.
* Checking touchpoint order values.
* Confirming that calculated metrics are logically consistent.

SQL results should also be reviewed to ensure that the calculated metrics match their intended business definitions.

---

# 18. Relationship Between SQL and Dashboard

The SQL analysis supports the dashboard by providing calculated KPI values and summarized datasets.

The relationship can be represented as:

```text
Cleaned Dataset
      ↓
SQL Database Table
      ↓
SQL Queries
      ↓
Calculated KPIs
      ↓
Dashboard Visualizations
      ↓
Performance Analysis
      ↓
Business Insights
      ↓
Business Recommendations
```

### Dashboard Metrics Supported by SQL

The SQL queries provide metrics that can support:

* KPI cards
* Campaign comparison charts
* Marketing channel comparison charts
* Revenue trend charts
* Conversion trend charts
* Customer journey analysis
* Attribution analysis
* Profit analysis
* Budget analysis
* CPA analysis
* ROI analysis
* Performance rating analysis

---

# 19. Business Value

The SQL analysis provides several important areas of business value.

### Customer Acquisition Efficiency

CPA analysis helps determine the cost of acquiring customers and allows comparisons between campaigns and marketing channels.

### Marketing Channel Performance

Comparing CPA, ROI, revenue, profit, conversions, and touchpoints across channels helps identify stronger and weaker marketing channels.

### Campaign Performance

Campaign-level revenue, profit, cost, budget, CPA, and conversion analysis provides a detailed view of campaign effectiveness.

### Customer Value

Revenue per customer and profit per customer help measure the financial value generated by customers.

### Customer Journey Analysis

Customer journey length, touchpoint distribution, and common customer journeys help explain how customers interact with marketing channels.

### Conversion Analysis

Overall conversion rate, campaign conversion rate, channel conversion rate, monthly conversion trends, and conversions by touchpoint order provide insight into conversion performance.

### Attribution Analysis

First-touch and last-touch attribution help identify channels and campaigns that frequently initiate or conclude customer journeys.

### Financial Performance

Revenue, profit, budget, campaign cost, CPA, and ROI provide a financial view of marketing effectiveness.

### Time-Based Analysis

Monthly revenue and conversion trends help identify changes in marketing performance over time.

---

# 20. Reproducibility

The SQL analysis is designed to provide reproducible calculations from the project database table.

Each SQL query has a defined purpose and uses explicit SQL functions, filters, grouping, sorting, and aggregation logic.

The documentation identifies:

* Query file name.
* Metric calculated.
* Purpose of the query.
* Columns used.
* Filtering conditions.
* Aggregation logic.
* Grouping logic.
* Sorting logic.
* Business interpretation.

This makes the SQL analysis easier for team members and reviewers to understand and reproduce.

---

# 21. SQL Query Summary

| Query File                                    | Main Metric / Analysis        | Analysis Level     |
| --------------------------------------------- | ----------------------------- | ------------------ |
| `Average_CPA.sql`                             | Average CPA                   | Overall            |
| `Average_CPA_by_Campaign.sql`                 | Average CPA                   | Campaign           |
| `Average_CPA_by_Marketing_Channel.sql`        | Average CPA                   | Channel            |
| `Average_Customer_Journey_Length.sql`         | Average Touchpoints           | Customer           |
| `Average_Profit_per_customer.sql`             | Profit per Customer           | Customer           |
| `Average_ROI.sql`                             | Average ROI                   | Overall            |
| `Average_ROI_by_Campaign.sql`                 | Average ROI                   | Campaign — Pending |
| `Average_ROI_by_Marketing_Channel.sql`        | Average ROI                   | Channel            |
| `Average_Time_to_Conversion.sql`              | Average Days to Conversion    | Converted Customer |
| `Average_revnue_per_customer.sql`             | Revenue per Customer          | Customer           |
| `Budget_Allocation_by_Campaign.sql`           | Total Budget                  | Campaign           |
| `Campaign_Cost_by_Campaign.sql`               | Campaign Cost                 | Campaign           |
| `Conversion_Rate_by_Campaign.sql`             | Conversion Rate               | Campaign           |
| `Conversion_Rate_by_Marketing_Channel.sql`    | Conversion Rate               | Channel            |
| `Conversion_by_Marketing_Chanel.sql`          | Total Conversions             | Channel            |
| `Conversions_by_Campaign.sql`                 | Total Conversions             | Campaign           |
| `conversions_by_Touchpoint_Order.sql`         | Total Conversions             | Touchpoint Order   |
| `Customer_Journey_Length_by_User.sql`         | Touchpoints                   | Customer           |
| `Customers_Longest_Conversion_Journey.sql`    | Longest Journey               | Top 10 Customers   |
| `Customers_Longest_Conversion_Time.sql`       | Longest Conversion Time       | Top 10 Customers   |
| `First-Touch_Attribution_by_Campaign.sql`     | First-Touch Count             | Campaign           |
| `First-Touch_Attribution_by_Channel.sql`      | First-Touch Count             | Channel            |
| `Last-Touch_Attribution_by_Campaign.sql`      | Last-Touch Count              | Campaign           |
| `Last-Touch_Attribution_by_Channel.sql`       | Last-Touch Count              | Channel            |
| `Monthly_Conversion_Trend.sql`                | Conversion Trend              | Monthly            |
| `Monthly_Revenue_Trend.sql`                   | Revenue Trend                 | Monthly            |
| `Monthly_Revenue_by_Marketing_Channel.sql`    | Revenue Trend                 | Monthly + Channel  |
| `Most_Common_Customer_Journey.sql`            | Journey Frequency             | Customer Journey   |
| `Overall_Conversion_Rate.sql`                 | Conversions + Conversion Rate | Overall            |
| `Performance_Rating_by_Campaign.sql`          | Rating Frequency              | Campaign           |
| `Performance_Rating_by_Marketing_Channel.sql` | Rating Frequency              | Channel            |
| `Profit_by_Campaign.sql`                      | Total Profit                  | Campaign           |
| `Profit_by_Marketing_Channel.sql`             | Total Profit                  | Channel            |
| `Revenue_by_Campaign.sql`                     | Total Revenue                 | Campaign           |
| `Revenue_by_Marketing_Channel.sql`            | Total Revenue                 | Channel            |
| `Total_Budget.sql`                            | Total Budget                  | Overall            |
| `Total_Customer.sql`                          | Total Customers               | Overall            |
| `Total_Revenue.sql`                           | Total Revenue                 | Overall            |
| `Total_campaign_cost.sql`                     | Total Campaign Cost           | Overall            |
| `Total_conversions.sql`                       | Total Conversions             | Overall            |
| `Total_marketing_touchpoints.sql`             | Total Touchpoints             | Overall            |
| `Total_profit.sql`                            | Total Profit                  | Overall            |
| `Touchpoint_order_distribution.sql`           | Touchpoint Frequency          | Touchpoint Order   |
| `Touchpoints_by_Marketing_Channel.sql`        | Total Touchpoints             | Channel            |

---

# 22. Conclusion

The SQL analysis forms an important part of the **Multi-Touch Marketing Attribution & ROI Dashboard** project.

The implemented SQL queries provide a comprehensive analysis of marketing performance across customer acquisition, campaigns, channels, conversions, revenue, profit, budget, ROI, customer journeys, and attribution.

The analysis also provides time-based insights through monthly conversion and revenue trends.

The SQL results can be used to support dashboard visualizations and help identify important business patterns, including high-performing channels, cost-efficient campaigns, revenue and profit contributors, customer journey behavior, and conversion trends.

The `Average_ROI_by_Campaign.sql` file is currently empty and should be implemented if campaign-level ROI analysis is required for the final dashboard or project report.
