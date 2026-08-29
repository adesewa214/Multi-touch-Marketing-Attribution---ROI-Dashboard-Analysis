WITH LastTouch AS
(
    SELECT *,
           ROW_NUMBER() OVER
           (
               PARTITION BY User_ID
               ORDER BY Touchpoint_Order DESC
           ) AS rn
    FROM dbo.Multi_touch_market_attribution
)

SELECT
    Channel,
    COUNT(*) AS Last_Touch_Count
FROM LastTouch
WHERE rn = 1
GROUP BY Channel
ORDER BY Last_Touch_Count DESC