SELECT
    Campaign,
    ROUND(SUM(Campaign_Cost_USD),2) AS Total_Campaign_Cost
FROM dbo.Multi_touch_market_attribution
GROUP BY Campaign
ORDER BY Total_Campaign_Cost DESC