SELECT
    Channel,
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY Channel
ORDER BY Total_Conversions DESC