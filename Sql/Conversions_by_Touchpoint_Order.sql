SELECT
    Touchpoint_Order,
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY Touchpoint_Order
ORDER BY Touchpoint_Order