SELECT
ROUND(
SUM(Profit_USD)
/ COUNT(DISTINCT User_ID),
2
) AS Profit_Per_Customer
FROM dbo.Multi_touch_market_attribution;