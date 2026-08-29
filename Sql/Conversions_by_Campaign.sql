SELECT
    Campaign,
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY Campaign
ORDER BY Total_Conversions DESC