WITH LastTouch AS
(
    SELECT
        User_ID,
        Campaign,
        Touchpoint_Order,
        ROW_NUMBER() OVER
        (
            PARTITION BY User_ID
            ORDER BY Touchpoint_Order DESC
        ) AS rn
    FROM dbo.Multi_touch_market_attribution
)

SELECT
    Campaign,
    COUNT(*) AS Last_Touch_Count
FROM LastTouch
WHERE rn = 1
GROUP BY Campaign
ORDER BY Last_Touch_Count DESC