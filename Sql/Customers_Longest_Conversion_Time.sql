--Top 10 Customers with the Longest Conversion Time
SELECT TOP 10
    User_ID,
    DATEDIFF
    (
        DAY,
        MIN([Timestamp]),
        MAX([Timestamp])
    ) AS Days_To_Convert
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1
GROUP BY User_ID
ORDER BY Days_To_Convert DESC;

