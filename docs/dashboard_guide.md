# Dashboard Guide

## 1. Dashboard Overview

The Multi-Touch Marketing Attribution & ROI Dashboard provides an interactive view of marketing performance across different channels, campaigns, customers, and time periods.

The dashboard is designed to help users understand:

* How marketing channels perform
* Which campaigns generate conversions
* How much revenue is generated
* How much is spent on campaigns
* How profitable marketing activities are
* Which channels and campaigns provide better ROI and ROAS
* How efficiently customers are acquired
* How marketing performance changes over time

The dashboard combines cleaned marketing data, calculated KPIs, SQL analysis, and visualizations to provide a centralized view of marketing performance.

---

## 2. Dashboard Objectives

The primary objectives of the dashboard are:

1. Monitor overall marketing performance.
2. Compare marketing channels.
3. Compare marketing campaigns.
4. Track conversions.
5. Analyze revenue and marketing costs.
6. Evaluate profitability.
7. Measure ROI and ROAS.
8. Monitor customer acquisition efficiency.
9. Identify high-performing and low-performing marketing activities.
10. Support data-driven marketing decisions.

---

## 3. Dashboard Data Source

The dashboard uses the cleaned Multi-Touch Marketing Attribution dataset.

The primary cleaned dataset is:

```text
data/cleaned/cleaned_multi_touch_attribution_data.csv
```

The Excel version is:

```text
data/cleaned/cleaned_multi_touch_attribution_data.xlsx
```

The cleaned dataset contains 10,000 records and 11 columns.

The main fields used for dashboard analysis include:

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

The project also uses marketing performance fields such as:

```text
Campaign_Cost_USD
Budget_USD
Revenue_USD
Profit_USD
ROI_%
ROAS
CPA_USD
Performance_Rating
```

These fields support the financial and marketing performance analysis represented in the dashboard.

---

## 4. Dashboard Users

The dashboard can be useful for different stakeholders.

### Marketing Managers

Marketing managers can use the dashboard to:

* Compare channel performance
* Monitor campaign results
* Identify inefficient campaigns
* Review marketing costs
* Evaluate ROI and ROAS
* Make budget allocation decisions

### Business Analysts

Business analysts can use the dashboard to:

* Investigate marketing trends
* Compare KPIs
* Identify patterns
* Analyze customer journeys
* Generate business insights

### Marketing Teams

Marketing teams can use the dashboard to:

* Monitor campaign performance
* Identify successful channels
* Track conversions
* Review customer interactions

### Management

Management can use the dashboard for a high-level view of:

* Revenue
* Profit
* Marketing spending
* Conversion performance
* ROI
* ROAS
* Overall marketing effectiveness

---

# 5. Dashboard KPI Cards

The dashboard should provide high-level KPI cards to summarize marketing performance.

Important KPI cards include:

* Total Customers
* Total Conversions
* Conversion Rate
* Total Marketing Touchpoints
* Total Revenue
* Total Campaign Cost
* Total Budget
* Total Profit
* Average CPA
* Average ROI
* ROAS

These KPI cards provide an immediate overview before users investigate individual channels or campaigns.

---

## 6. Total Customers

The Total Customers KPI represents the number of unique users in the dataset.

The calculation uses unique `User ID` values.

```text
Total Customers = COUNT(DISTINCT User ID)
```

This prevents users with multiple touchpoints from being counted multiple times.

### Interpretation

A higher number indicates a larger customer population represented in the marketing dataset.

---

## 7. Total Conversions

Total Conversions represents the number of recorded conversions.

For this project, a conversion is represented by:

```text
Conversion = "Yes"
```

### Interpretation

This KPI indicates the overall number of recorded conversions associated with the marketing interactions.

---

## 8. Conversion Rate

Conversion Rate measures the percentage of marketing touchpoints resulting in a conversion.

```text
Conversion Rate (%) =
(Total Conversions / Total Marketing Touchpoints) × 100
```

### Interpretation

A higher conversion rate indicates that a larger proportion of recorded interactions resulted in conversions.

Conversion rate should be evaluated together with cost, revenue, and profit.

---

# 9. Total Marketing Touchpoints

Total Marketing Touchpoints represents the number of recorded marketing interactions.

Each dataset record represents a marketing touchpoint.

### Interpretation

This KPI is particularly important for a multi-touch attribution project because a user may interact with multiple marketing channels before conversion.

---

# 10. Total Revenue

Total Revenue represents the total revenue associated with the marketing activities.

```text
Total Revenue = SUM(Revenue_USD)
```

### Interpretation

Higher revenue indicates stronger financial contribution from the analyzed marketing activities.

Revenue should be compared with marketing costs and profit to evaluate financial effectiveness.

---

# 11. Total Campaign Cost

Total Campaign Cost represents the total amount spent on marketing campaigns.

```text
Total Campaign Cost = SUM(Campaign_Cost_USD)
```

### Interpretation

This KPI helps users understand the total marketing investment associated with the analyzed campaigns.

---

# 12. Total Budget

Total Budget represents the total planned budget allocated to the campaigns.

```text
Total Budget = SUM(Budget_USD)
```

### Interpretation

Comparing campaign cost with budget can help identify whether marketing activities are operating within planned spending levels.

---

# 13. Total Profit

Total Profit represents the total financial profit generated from marketing activities.

```text
Total Profit = SUM(Profit_USD)
```

Profit can generally be represented as:

```text
Profit = Revenue - Campaign Cost
```

### Interpretation

A positive profit indicates that revenue exceeded associated campaign costs.

A negative profit indicates that campaign costs exceeded generated revenue.

---

# 14. Average CPA

CPA stands for Cost Per Acquisition.

It measures the average cost associated with generating a conversion.

The overall calculation can be represented as:

```text
CPA = Total Campaign Cost / Total Conversions
```

The project can also use the existing:

```text
CPA_USD
```

field to calculate average CPA.

```text
Average CPA = AVG(CPA_USD)
```

### Interpretation

Lower CPA generally indicates more efficient customer acquisition.

---

# 15. Average ROI

ROI stands for Return on Investment.

A standard marketing ROI formula is:

```text
ROI (%) =
((Revenue - Campaign Cost) / Campaign Cost) × 100
```

The project also contains the:

```text
ROI_%
```

field.

Therefore, average ROI can be calculated as:

```text
Average ROI = AVG(ROI_%)
```

### Interpretation

A higher positive ROI indicates stronger financial return relative to marketing investment.

---

# 16. ROAS

ROAS stands for Return on Ad Spend.

```text
ROAS = Revenue / Campaign Cost
```

### Example

If:

```text
Revenue = $10,000
Campaign Cost = $2,000
```

then:

```text
ROAS = 5
```

This means that every $1 spent generated $5 in revenue.

### Interpretation

Higher ROAS generally indicates stronger advertising efficiency.

---

# 17. Channel Analysis

The dashboard should allow users to compare the following marketing channels:

* Email
* Search Ads
* Social Media
* Direct Traffic
* Referral
* Display Ads

Channel-level analysis can include:

* Customers
* Touchpoints
* Conversions
* Conversion rate
* Revenue
* Campaign cost
* Profit
* CPA
* ROI
* ROAS

---

## 18. Channel Performance Interpretation

Users can compare channels to identify:

### High-Converting Channels

Channels generating a high number of conversions can be investigated for successful customer acquisition strategies.

### High-Revenue Channels

Channels generating high revenue may contribute strongly to business growth.

### Low-Cost Channels

Channels with lower acquisition costs may provide greater efficiency.

### High-ROI Channels

Channels with higher ROI may provide stronger financial returns.

### High-ROAS Channels

Channels with high ROAS may be more efficient from an advertising-spend perspective.

A channel should not be classified as the "best" based on a single KPI. Multiple performance indicators should be considered together.

---

# 19. Campaign Analysis

The dashboard can be used to compare marketing campaigns.

The final campaign categories include:

* New Product Launch
* Winter Sale
* Brand Awareness
* Retargeting
* Discount Offer
* No Campaign

Campaign-level analysis can include:

* Conversions
* Conversion rate
* Revenue
* Campaign cost
* Profit
* CPA
* ROI
* ROAS
* Performance rating

---

# 20. Campaign Performance Interpretation

Campaigns can be evaluated based on multiple dimensions.

For example:

### Conversion Performance

Which campaigns generate the most conversions?

### Financial Performance

Which campaigns generate the highest revenue and profit?

### Cost Efficiency

Which campaigns achieve conversions at a lower CPA?

### Investment Efficiency

Which campaigns generate stronger ROI?

### Advertising Efficiency

Which campaigns generate stronger ROAS?

Combining these metrics provides a more complete assessment of campaign performance.

---

# 21. Time-Based Analysis

The cleaned dataset contains several date and time fields:

```text
Date
Year
Month
Day
Hour
```

These fields enable time-based dashboard analysis.

Examples include:

* Daily conversions
* Monthly conversions
* Monthly revenue
* Monthly campaign cost
* Monthly profit
* Monthly ROI
* Monthly ROAS
* Hourly interaction trends

---

# 22. Monthly Trend Analysis

Monthly analysis can be used to identify changes in marketing performance over time.

Users can compare:

* Monthly conversions
* Monthly revenue
* Monthly cost
* Monthly profit
* Monthly ROI
* Monthly ROAS

### Business Use

Monthly trend analysis can help identify:

* Strong-performing months
* Weak-performing months
* Seasonal patterns
* Changes in campaign effectiveness
* Periods requiring additional investigation

---

# 23. Customer Journey Analysis

The project follows a multi-touch attribution approach.

Users may interact with multiple marketing channels before converting.

For example:

```text
Email
   ↓
Social Media
   ↓
Search Ads
   ↓
Conversion
```

The `Touchpoint_Order` field helps represent the sequence of interactions.

This can be used to understand:

* First interactions
* Later interactions
* Number of touchpoints
* Channel sequences
* Customer journeys leading to conversion

---

# 24. Multi-Touch Attribution Analysis

Multi-touch attribution evaluates the contribution of multiple marketing interactions rather than assigning all credit to a single touchpoint.

The dashboard can be used to investigate:

* Which channels appear frequently in converting journeys
* Which channels are involved early in customer journeys
* Which channels are involved closer to conversion
* How many touchpoints occur before conversion
* Which campaigns frequently appear in successful journeys

This provides a broader understanding of marketing influence.

---

# 25. Dashboard Filters

Where filters are available, users can narrow the analysis based on fields such as:

### Channel

Select one or more marketing channels.

### Campaign

Select specific campaigns.

### Conversion

Filter between:

```text
Yes
No
```

### Date

Select a particular time period.

### Year

Filter analysis by year.

### Month

Analyze performance for specific months.

These filters allow users to investigate specific segments without changing the underlying dataset.

---

# 26. Recommended Dashboard Filtering Workflow

A recommended workflow is:

### Step 1 — Review Overall KPIs

Start with the main KPI cards.

Review:

* Customers
* Conversions
* Conversion Rate
* Revenue
* Cost
* Profit
* ROI
* ROAS

### Step 2 — Select a Time Period

Use date, year, or month filters if available.

### Step 3 — Compare Channels

Review channel-level conversion and financial performance.

### Step 4 — Compare Campaigns

Identify campaigns with stronger or weaker results.

### Step 5 — Investigate Customer Journeys

Review touchpoint patterns and channel sequences.

### Step 6 — Evaluate Financial Efficiency

Compare:

* CPA
* ROI
* ROAS
* Profit

### Step 7 — Develop Business Recommendations

Use the combined results to identify opportunities for optimization.

---

# 27. How to Interpret the Dashboard

The dashboard should be interpreted from a high-level perspective first and then investigated at a more detailed level.

Recommended order:

```text
Overall KPIs
     ↓
Time Trends
     ↓
Channel Performance
     ↓
Campaign Performance
     ↓
Customer Journey
     ↓
Financial Efficiency
     ↓
Business Recommendations
```

This approach prevents users from making decisions based on a single chart or metric.

---

# 28. Example Business Questions

The dashboard can help answer questions such as:

### Customer Questions

* How many unique customers are represented?
* How many customers converted?
* How many touchpoints occur before conversion?

### Channel Questions

* Which channel generates the most conversions?
* Which channel generates the most revenue?
* Which channel has the lowest CPA?
* Which channel has the highest ROI?
* Which channel has the highest ROAS?

### Campaign Questions

* Which campaign generates the most conversions?
* Which campaign generates the highest revenue?
* Which campaign generates the highest profit?
* Which campaign is most cost-efficient?

### Financial Questions

* How much was spent on campaigns?
* How much revenue was generated?
* What is the total marketing profit?
* Is marketing spending within budget?
* What is the overall ROI?
* What is the overall ROAS?

### Trend Questions

* Which months have the highest conversions?
* How does revenue change over time?
* Are campaign costs increasing?
* Which periods show stronger ROI?

---

# 29. Business Decision Framework

The dashboard should support decisions based on multiple KPIs.

For example:

```text
High Conversions
+
High Revenue
+
Positive Profit
+
Strong ROI
+
Strong ROAS
+
Acceptable CPA
```

can indicate a potentially strong marketing activity.

However:

```text
High Conversions
+
High Campaign Cost
+
Low Profit
+
Low ROI
```

may indicate that the campaign generates activity but is not financially efficient.

Therefore, conversion performance and financial performance should always be considered together.

---

# 30. Dashboard Best Practices

Users should follow these practices when interpreting the dashboard:

1. Do not rely on a single KPI.
2. Compare revenue with marketing cost.
3. Consider both conversion volume and conversion rate.
4. Compare CPA with revenue and customer value.
5. Evaluate ROI and ROAS together.
6. Use filters to investigate specific channels and campaigns.
7. Review trends over time.
8. Consider customer journeys in a multi-touch environment.
9. Investigate unusually high or low values.
10. Validate findings against the underlying dataset when necessary.

---

# 31. Dashboard Limitations

The dashboard should be interpreted within the limitations of the available dataset.

Important considerations include:

* The dataset represents recorded marketing touchpoints.
* A single user may have multiple touchpoints.
* Conversion attribution may involve multiple interactions.
* KPI results depend on the accuracy of the underlying data.
* ROI and ROAS depend on the quality of revenue and campaign-cost information.
* A high number of touchpoints does not automatically indicate high marketing effectiveness.
* Correlation between a channel and conversion does not necessarily prove that the channel independently caused the conversion.

These limitations should be considered when making business recommendations.

---

# 32. Data Refresh Process

When the source dataset is updated, the following process should be followed:

```text
Updated Raw Dataset
        ↓
Run Data Cleaning Script
        ↓
Generate Cleaned Dataset
        ↓
Validate Data Quality
        ↓
Update SQL Analysis
        ↓
Refresh Dashboard
        ↓
Review KPIs
```

The data-cleaning script is located at:

```text
scripts/data_cleaning.py
```

The raw dataset is located at:

```text
data/raw/multi_touch_attribution_data.csv
```

The cleaned dataset is generated under:

```text
data/cleaned/
```

---

# 33. Dashboard Documentation Summary

The dashboard provides a centralized view of marketing performance using cleaned and structured marketing data.

It combines:

* Customer analysis
* Conversion analysis
* Channel analysis
* Campaign analysis
* Time-based analysis
* Financial analysis
* ROI analysis
* ROAS analysis
* CPA analysis
* Multi-touch customer journey analysis

The dashboard is intended to transform the underlying marketing data into actionable insights that can support marketing optimization and budget allocation decisions.

---

# 34. Key Takeaways

The dashboard enables users to:

* Monitor overall marketing performance.
* Track customer and conversion metrics.
* Compare marketing channels.
* Compare campaigns.
* Analyze revenue and marketing expenditure.
* Evaluate profitability.
* Measure ROI.
* Measure ROAS.
* Monitor CPA.
* Analyze customer touchpoints.
* Investigate customer journeys.
* Identify marketing trends.
* Support data-driven decision-making.

The dashboard should be used as an analytical decision-support tool, with conclusions based on multiple KPIs and supporting analysis rather than individual metrics alone.
