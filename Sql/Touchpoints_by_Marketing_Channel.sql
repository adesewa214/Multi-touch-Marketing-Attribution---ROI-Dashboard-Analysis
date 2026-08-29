SELECT
    Channel,
    COUNT(*) AS Total_Touchpoints
FROM dbo.Multi_touch_market_attribution
GROUP BY Channel
ORDER BY Total_Touchpoints DESC