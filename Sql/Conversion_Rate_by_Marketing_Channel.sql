SELECT
    Channel,
    ROUND(
        100.0 * COUNT(CASE WHEN Conversion = 1 THEN 1 END) / COUNT(*),
        2
    ) AS Conversion_Rate
FROM dbo.Multi_touch_market_attribution
GROUP BY Channel
ORDER BY Conversion_Rate DESC