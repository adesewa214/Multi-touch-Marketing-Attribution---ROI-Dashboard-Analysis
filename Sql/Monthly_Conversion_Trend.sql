SELECT
    YEAR([Timestamp]) AS [Year],
    MONTH([Timestamp]) AS [Month],
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY
    YEAR([Timestamp]),
    MONTH([Timestamp])
ORDER BY
    [Year],
    [Month]