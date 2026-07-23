SELECT
    Campaign,
    ROUND(SUM(Profit_USD),2) AS Total_Profit
FROM dbo.Multi_touch_market_attribution
GROUP BY Campaign
ORDER BY Total_Profit DESC