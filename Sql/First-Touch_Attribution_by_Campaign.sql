SELECT
    Campaign,
    COUNT(*) AS First_Touch_Count
FROM dbo.Multi_touch_market_attribution
WHERE Touchpoint_Order = 1
GROUP BY Campaign
ORDER BY First_Touch_Count DESC