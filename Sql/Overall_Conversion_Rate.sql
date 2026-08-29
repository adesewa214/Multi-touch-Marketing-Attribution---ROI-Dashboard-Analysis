--overall conversion rateg
SELECT
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1;

--conversion rate percentage
SELECT
    CAST(
        100.0 *
        COUNT(CASE WHEN Conversion = 1 THEN 1 END)
        / COUNT(*)
        AS DECIMAL(5,2)
    ) AS Conversion_Rate_Percentage
FROM dbo.Multi_touch_market_attribution;