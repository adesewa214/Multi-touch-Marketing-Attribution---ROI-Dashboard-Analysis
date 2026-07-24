SELECT
    YEAR([Timestamp]) AS [Year],
    MONTH([Timestamp]) AS [Month],
    ROUND(SUM(Revenue_USD),2) AS Total_Revenue
FROM dbo.Multi_touch_market_attribution
GROUP BY
    YEAR([Timestamp]),
    MONTH([Timestamp])
ORDER BY
    [Year],
    [Month]