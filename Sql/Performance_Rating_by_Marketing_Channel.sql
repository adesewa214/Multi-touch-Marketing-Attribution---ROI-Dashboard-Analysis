SELECT
    Channel,
    Performance_Rating,
    COUNT(*) AS Frequency
FROM dbo.Multi_touch_market_attribution
GROUP BY
    Channel,
    Performance_Rating
ORDER BY
    Channel,
    Frequency DESC