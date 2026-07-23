SELECT
    Campaign,
    ROUND(SUM(Budget_USD),2) AS Total_Budget
FROM dbo.Multi_touch_market_attribution
GROUP BY Campaign
ORDER BY Total_Budget DESC