SELECT
    Channel,
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM dbo.Multi_touch_market_attribution
GROUP BY Channel
ORDER BY Total_Revenue DESC
