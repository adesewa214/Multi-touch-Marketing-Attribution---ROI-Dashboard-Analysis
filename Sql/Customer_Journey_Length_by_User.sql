SELECT
    User_ID,
    COUNT(*) AS Total_Touchpoints
FROM dbo.Multi_touch_market_attribution
GROUP BY User_ID
ORDER BY Total_Touchpoints DESC;