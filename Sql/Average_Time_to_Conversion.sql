SELECT
    ROUND(AVG(CAST(Days_To_Convert AS FLOAT)),2) AS Average_Days
FROM
(SELECT
     User_ID,
     DATEDIFF
     (
       DAY,
       MIN([Timestamp]),
       MAX([Timestamp])
      ) AS Days_To_Convert
      FROM dbo.Multi_touch_market_attribution   WHERE Conversion = 1
      GROUP BY User_ID
) A