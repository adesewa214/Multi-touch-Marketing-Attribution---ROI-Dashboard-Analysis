SELECT
    Touchpoint_Order,
    COUNT(*) AS Frequency
FROM dbo.Multi_touch_market_attribution
GROUP BY Touchpoint_Order
ORDER BY Touchpoint_Order;