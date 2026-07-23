SELECT
    Campaign,
    Performance_Rating,
    COUNT(*) AS Frequency
FROM dbo.Multi_touch_market_attribution
GROUP BY
    Campaign,
    Performance_Rating
ORDER BY
    Campaign,
    Frequency DESC