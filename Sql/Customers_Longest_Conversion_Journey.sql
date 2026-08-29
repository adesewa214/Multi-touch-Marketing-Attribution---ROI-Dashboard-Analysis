--Top 10 Customers with the Longest Conversion Journey
SELECT TOP 10
    User_ID,
    COUNT(*) AS Total_Touchpoints
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY User_ID
ORDER BY Total_Touchpoints DESC