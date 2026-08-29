SELECT
    Channel,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM dbo.Multi_touch_market_attribution
GROUP BY Channel
ORDER BY Total_Profit DESC