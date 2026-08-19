# KPI Definitions

## 1. Overview

Key Performance Indicators (KPIs) are measurable values used to evaluate the effectiveness and efficiency of marketing activities.

In the Multi-Touch Marketing Attribution & ROI Dashboard project, KPIs are used to analyze:

* Customer conversions
* Marketing touchpoints
* Revenue generated
* Campaign costs
* Marketing profit
* Return on Investment (ROI)
* Return on Ad Spend (ROAS)
* Cost per Acquisition (CPA)
* Campaign performance

These KPIs help identify high-performing channels and campaigns and support data-driven marketing decisions.

---

## 2. KPI Categories

The project's KPIs can be grouped into the following categories:

### Conversion KPIs

* Total Conversions
* Overall Conversion Rate

### Customer KPIs

* Total Customers

### Engagement KPIs

* Total Marketing Touchpoints

### Financial KPIs

* Total Revenue
* Total Campaign Cost
* Total Marketing Profit
* Total Budget

### Efficiency KPIs

* Average CPA
* Average ROI
* ROAS

These KPIs can be analyzed at the overall level and, where applicable, by channel, campaign, and time period.

---

# 3. Total Customers

## Definition

Total Customers represents the number of unique users present in the dataset.

Because the same user may interact with multiple marketing channels, counting rows would overstate the number of customers. Therefore, unique `User ID` values are counted.

## Formula

```text
Total Customers = COUNT(DISTINCT User ID)
```

## Purpose

This KPI helps measure the size of the customer population represented in the dataset.

## Business Interpretation

A higher number of unique customers indicates a broader customer base represented in the marketing data.

This KPI can also be compared across time periods and marketing channels to understand customer acquisition patterns.

## Example

If the dataset contains:

```text
User ID:
U001
U002
U001
U003
```

The total number of customers is:

```text
3
```

because `U001` appears more than once but represents only one unique customer.

---

# 4. Total Conversions

## Definition

Total Conversions represents the number of records where the `Conversion` value is `Yes`.

## Formula

```text
Total Conversions = COUNT(Conversion = "Yes")
```

## Purpose

This KPI measures the total number of recorded conversions.

## Business Interpretation

A higher number of conversions generally indicates stronger marketing performance, although conversions should also be evaluated relative to marketing costs, customer volume, and traffic.

## Example

If the conversion column contains:

```text
Yes
No
Yes
No
Yes
```

then:

```text
Total Conversions = 3
```

---

# 5. Overall Conversion Rate

## Definition

Overall Conversion Rate measures the percentage of marketing touchpoints that resulted in a conversion.

## Formula

```text
Conversion Rate (%) =
(Total Conversions / Total Marketing Touchpoints) × 100
```

## Purpose

This KPI measures the proportion of recorded touchpoints associated with conversions.

## Business Interpretation

A higher conversion rate indicates that a larger proportion of the measured interactions resulted in conversions.

Conversion rate should be evaluated together with other KPIs because a high conversion rate does not necessarily mean that a campaign is financially profitable.

## Example

If:

```text
Total Conversions = 2,000
Total Touchpoints = 10,000
```

then:

```text
Conversion Rate =
(2,000 / 10,000) × 100
= 20%
```

---

# 6. Total Marketing Touchpoints

## Definition

Total Marketing Touchpoints represents the total number of marketing interaction records in the dataset.

Each row represents one recorded touchpoint.

## Formula

```text
Total Marketing Touchpoints = COUNT(*) 
```

or:

```text
Total Marketing Touchpoints = Number of dataset records
```

## Purpose

This KPI measures the overall volume of marketing interactions.

## Business Interpretation

A high number of touchpoints indicates a large volume of recorded marketing activity.

This KPI is especially important for a multi-touch attribution project because users may interact with multiple channels before conversion.

---

# 7. Total Revenue

## Definition

Total Revenue represents the total revenue generated from the marketing activities represented in the dataset.

## Formula

```text
Total Revenue = SUM(Revenue_USD)
```

## Purpose

This KPI measures the total monetary value generated.

## Business Interpretation

Higher revenue indicates greater financial contribution from the analyzed marketing activities.

Revenue should be compared with campaign cost and budget to determine whether marketing activity is financially efficient.

---

# 8. Total Campaign Cost

## Definition

Total Campaign Cost represents the total amount spent on the campaigns represented in the dataset.

## Formula

```text
Total Campaign Cost = SUM(Campaign_Cost_USD)
```

## Purpose

This KPI measures total marketing expenditure.

## Business Interpretation

The KPI helps organizations understand how much was spent to generate the observed marketing activity and conversions.

It can be compared with:

* Revenue
* Profit
* ROI
* ROAS
* Conversion count

to evaluate marketing efficiency.

---

# 9. Total Budget

## Definition

Total Budget represents the combined planned marketing budget associated with the campaigns.

## Formula

```text
Total Budget = SUM(Budget_USD)
```

## Purpose

This KPI measures the total planned spending available for the marketing campaigns.

## Business Interpretation

Comparing total budget with actual campaign cost helps determine whether marketing spending remained within planned limits.

For example:

```text
Budget > Campaign Cost
```

may indicate that spending remained below the allocated budget.

Where:

```text
Campaign Cost > Budget
```

it may indicate budget overspending.

---

# 10. Total Marketing Profit

## Definition

Total Marketing Profit represents the total profit generated after accounting for campaign costs.

## Formula

```text
Total Profit = SUM(Profit_USD)
```

Where profit is generally represented as:

```text
Profit = Revenue - Campaign Cost
```

## Purpose

This KPI measures the financial outcome of marketing activity.

## Business Interpretation

A positive total profit indicates that the analyzed marketing activities generated more revenue than their associated campaign costs.

A negative total profit indicates that campaign costs exceeded the generated revenue.

---

# 11. Average CPA

## Definition

CPA stands for **Cost Per Acquisition**.

Cost Per Acquisition measures the average marketing cost associated with acquiring a customer or generating a conversion.

In this project, the dataset contains a `CPA_USD` field that represents CPA values.

## Formula

At the overall level, CPA can be calculated as:

```text
CPA = Total Campaign Cost / Total Conversions
```

When analyzing the existing CPA field:

```text
Average CPA = AVG(CPA_USD)
```

## Purpose

CPA measures the cost efficiency of customer acquisition.

## Business Interpretation

A lower CPA generally indicates that conversions are being generated at a lower acquisition cost.

A higher CPA indicates that more marketing expenditure is required to generate conversions.

CPA should be evaluated together with revenue and customer value because a higher CPA may still be acceptable if the acquired customers generate substantially higher revenue or profit.

## Example

If:

```text
Campaign Cost = $10,000
Conversions = 500
```

then:

```text
CPA = $10,000 / 500
    = $20
```

The average acquisition cost is therefore $20 per conversion.

---

# 12. Average ROI

## Definition

ROI stands for **Return on Investment**.

ROI measures the return generated relative to the marketing investment.

The dataset contains an `ROI_%` field for ROI analysis.

## Formula

A standard marketing ROI calculation is:

```text
ROI (%) =
((Revenue - Campaign Cost) / Campaign Cost) × 100
```

Since:

```text
Profit = Revenue - Campaign Cost
```

ROI can also be represented as:

```text
ROI (%) =
(Profit / Campaign Cost) × 100
```

When using the existing ROI field:

```text
Average ROI = AVG(ROI_%)
```

## Purpose

ROI evaluates whether marketing investment generated a positive financial return.

## Business Interpretation

### Positive ROI

Indicates that the marketing activity generated more revenue than its associated cost.

### Zero ROI

Indicates that revenue was equal to the associated investment.

### Negative ROI

Indicates that the marketing activity generated less revenue than its associated cost.

A higher ROI generally indicates stronger investment efficiency.

---

# 13. ROAS

## Definition

ROAS stands for **Return on Ad Spend**.

ROAS measures how much revenue is generated for every unit of advertising spend.

The dataset contains a `ROAS` field for this analysis.

## Formula

```text
ROAS =
Revenue / Campaign Cost
```

## Purpose

ROAS measures advertising efficiency.

## Business Interpretation

For example:

```text
ROAS = 4
```

means:

```text
$1 spent on advertising generated $4 in revenue.
```

A higher ROAS generally indicates stronger advertising efficiency.

---

# 14. ROI vs ROAS

ROI and ROAS are related but measure different aspects of marketing performance.

| KPI  | Formula                         | Main Focus                     |
| ---- | ------------------------------- | ------------------------------ |
| ROI  | `(Revenue - Cost) / Cost × 100` | Profitability                  |
| ROAS | `Revenue / Cost`                | Advertising revenue efficiency |

### Example

Suppose:

```text
Revenue = $10,000
Campaign Cost = $2,000
```

Then:

```text
ROAS = $10,000 / $2,000
     = 5
```

ROI is:

```text
ROI = (($10,000 - $2,000) / $2,000) × 100
    = 400%
```

Therefore:

```text
ROAS = 5
ROI = 400%
```

ROAS focuses on revenue generated from advertising spend, while ROI considers the profit remaining after the investment.

---

# 15. Performance Rating

## Definition

`Performance_Rating` is a categorical indicator used to classify marketing performance.

It can be used to summarize whether a campaign or marketing activity is performing strongly or weakly based on the project's performance evaluation logic.

## Purpose

The performance rating provides a simplified way to communicate marketing performance to business users.

## Business Interpretation

Performance ratings can help stakeholders quickly identify:

* High-performing campaigns
* Average-performing campaigns
* Low-performing campaigns
* Areas requiring optimization

The rating should be interpreted together with the underlying numerical KPIs rather than used as the only performance measure.

---

# 16. KPI Analysis by Channel

KPIs can be grouped by the `Channel` column to compare marketing channels.

Important channel-level metrics include:

* Total conversions
* Conversion rate
* Total revenue
* Total campaign cost
* Total profit
* Average CPA
* Average ROI
* ROAS

Example analysis:

```text
Channel → Email
Channel → Search Ads
Channel → Social Media
Channel → Direct Traffic
Channel → Referral
Channel → Display Ads
```

This allows the team to determine which channels contribute most effectively to conversions and financial performance.

---

# 17. KPI Analysis by Campaign

KPIs can also be grouped by the `Campaign` column.

The campaign-level analysis can include:

* Conversion count
* Conversion rate
* Revenue
* Campaign cost
* Profit
* CPA
* ROI
* ROAS
* Performance rating

This allows marketing teams to identify campaigns that provide stronger financial and conversion outcomes.

---

# 18. KPI Analysis Over Time

The cleaned dataset contains several time-based fields:

* Date
* Year
* Month
* Day
* Hour

These fields allow KPIs to be analyzed over time.

Examples include:

* Monthly conversions
* Monthly revenue
* Monthly campaign cost
* Monthly profit
* Monthly ROI
* Monthly ROAS
* Hourly conversion trends

Time-based KPI analysis can help identify seasonal patterns, campaign trends, and periods of stronger or weaker performance.

---

# 19. KPI Dashboard Usage

The KPIs documented in this file can be displayed as summary cards, charts, tables, and filters in the project dashboard.

Recommended top-level KPI cards include:

```text
Total Customers
Total Conversions
Conversion Rate
Total Revenue
Total Campaign Cost
Total Profit
Average CPA
Average ROI
ROAS
Total Budget
Total Marketing Touchpoints
```

These KPIs provide a high-level overview of marketing performance.

---

# 20. KPI Calculation Considerations

KPI calculations should be performed carefully to avoid misleading results.

### Unique Customer Counting

Customers should be counted using distinct `User ID` values.

```text
COUNT(DISTINCT User ID)
```

This prevents users with multiple touchpoints from being counted multiple times.

### Conversion Counting

Conversions should be based on the appropriate conversion definition used by the project.

For the current dataset:

```text
Conversion = "Yes"
```

represents a conversion.

### Cost and Revenue

Cost and revenue should be aggregated consistently before calculating financial KPIs.

### Division by Zero

For metrics such as CPA, ROI, and ROAS, calculations should account for cases where campaign cost or conversions are zero.

For example:

```text
CPA = Total Cost / Total Conversions
```

should not be calculated when:

```text
Total Conversions = 0
```

Similarly:

```text
ROAS = Revenue / Campaign Cost
```

should not be calculated when:

```text
Campaign Cost = 0
```

---

# 21. KPI Summary Table

| KPI                 | Definition                                        | Formula                             | Unit     |
| ------------------- | ------------------------------------------------- | ----------------------------------- | -------- |
| Total Customers     | Number of unique users                            | `COUNT(DISTINCT User ID)`           | Count    |
| Total Conversions   | Number of converted records                       | `COUNT(Conversion = "Yes")`         | Count    |
| Conversion Rate     | Percentage of touchpoints resulting in conversion | `(Conversions / Touchpoints) × 100` | %        |
| Total Touchpoints   | Total marketing interactions                      | `COUNT(*)`                          | Count    |
| Total Revenue       | Total generated revenue                           | `SUM(Revenue_USD)`                  | USD      |
| Total Campaign Cost | Total marketing expenditure                       | `SUM(Campaign_Cost_USD)`            | USD      |
| Total Budget        | Total planned campaign budget                     | `SUM(Budget_USD)`                   | USD      |
| Total Profit        | Total marketing profit                            | `SUM(Profit_USD)`                   | USD      |
| Average CPA         | Average cost per acquisition                      | `AVG(CPA_USD)`                      | USD      |
| Average ROI         | Average return on investment                      | `AVG(ROI_%)`                        | %        |
| ROAS                | Revenue generated per unit of ad spend            | `Revenue / Campaign Cost`           | Ratio    |
| Performance Rating  | Categorical performance classification            | Project-defined logic               | Category |

---

# 22. Business Interpretation Framework

The KPIs should not be evaluated independently.

A strong marketing campaign should ideally demonstrate a combination of:

```text
High Conversions
        +
Strong Conversion Rate
        +
High Revenue
        +
Positive Profit
        +
Low/Acceptable CPA
        +
High ROI
        +
High ROAS
```

For example, a campaign with high conversions but very high costs may not be financially efficient.

Similarly, a campaign with high ROI but very few conversions may have limited overall business impact.

Therefore, multiple KPIs should be considered together when evaluating marketing performance.

---

# 23. Recommended Dashboard KPI Layout

A recommended dashboard structure is:

### Row 1 — Executive KPIs

```text
Total Customers
Total Conversions
Conversion Rate
Total Revenue
```

### Row 2 — Financial KPIs

```text
Campaign Cost
Total Profit
Total Budget
Average ROI
```

### Row 3 — Efficiency KPIs

```text
Average CPA
ROAS
Total Marketing Touchpoints
```

### Supporting Visualizations

The KPI cards can be supported by:

* Channel performance charts
* Campaign performance charts
* Monthly conversion trends
* Revenue vs cost analysis
* ROI comparison
* ROAS comparison
* Conversion funnel analysis
* Campaign performance tables

---

# 24. Data Fields Used for KPI Calculation

The following fields are particularly important for KPI calculations:

| Dataset Field        | KPI Usage                          |
| -------------------- | ---------------------------------- |
| `User ID`            | Total Customers                    |
| `Conversion`         | Total Conversions, Conversion Rate |
| `Revenue_USD`        | Total Revenue, ROI, ROAS           |
| `Campaign_Cost_USD`  | Campaign Cost, CPA, ROI, ROAS      |
| `Budget_USD`         | Total Budget                       |
| `Profit_USD`         | Total Profit, ROI                  |
| `ROI_%`              | Average ROI                        |
| `ROAS`               | ROAS                               |
| `CPA_USD`            | Average CPA                        |
| `Performance_Rating` | Performance evaluation             |
| `Channel`            | Channel-level KPI analysis         |
| `Campaign`           | Campaign-level KPI analysis        |
| `Date`               | Time-based KPI analysis            |
| `Year`               | Year-level KPI analysis            |
| `Month`              | Monthly KPI analysis               |
| `Hour`               | Hourly KPI analysis                |

---

# 25. Relationship Between KPIs and Business Decisions

The project's KPIs are intended to support practical marketing decisions.

| KPI Observation           | Possible Business Action                                |
| ------------------------- | ------------------------------------------------------- |
| High conversion rate      | Investigate and scale successful strategies             |
| Low conversion rate       | Review targeting, messaging, or customer journey        |
| High revenue              | Identify successful revenue-generating channels         |
| High campaign cost        | Review spending efficiency                              |
| High profit               | Consider increasing investment where appropriate        |
| Low CPA                   | Consider scaling efficient acquisition sources          |
| High ROI                  | Identify profitable investment opportunities            |
| High ROAS                 | Evaluate potential for increased advertising investment |
| Low ROAS                  | Review campaign spending and effectiveness              |
| High campaign performance | Analyze successful campaign characteristics             |
| Low campaign performance  | Optimize or reconsider campaign strategy                |

These recommendations should be supported by additional analysis rather than based on a single KPI.

---

# 26. Conclusion

The KPI framework provides a standardized method for measuring the performance of marketing channels and campaigns in the Multi-Touch Marketing Attribution & ROI Dashboard project.

The key metrics cover:

* Customer acquisition
* Conversion performance
* Marketing engagement
* Revenue generation
* Campaign expenditure
* Profitability
* Acquisition efficiency
* Investment efficiency
* Advertising efficiency

Together, these KPIs provide a comprehensive view of marketing performance and support the project's objective of identifying effective marketing channels and campaigns and improving data-driven decision-making.
