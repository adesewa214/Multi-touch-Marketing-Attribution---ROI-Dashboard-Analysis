SELECT
    Journey,
    COUNT(*) AS Frequency
FROM
(
    SELECT
        User_ID,
        STRING_AGG(Channel, ' → ')
        WITHIN GROUP (ORDER BY Touchpoint_Order) AS Journey
    FROM dbo.Multi_touch_market_attribution
    GROUP BY User_ID
) A
GROUP BY Journey
ORDER BY Frequency DESC