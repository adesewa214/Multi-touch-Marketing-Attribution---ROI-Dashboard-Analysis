SELECT
    ROUND(AVG(CAST(Touchpoints AS FLOAT)),2) AS Avg_Touchpoints
FROM
(
    SELECT
        User_ID,
        COUNT(*) AS Touchpoints
    FROM dbo.Multi_touch_market_attribution
    GROUP BY User_ID
) A