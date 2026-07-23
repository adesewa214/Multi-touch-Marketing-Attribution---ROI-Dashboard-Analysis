SELECT
ROUND(
SUM(Revenue_USD)
/ COUNT(DISTINCT User_ID),
2
) AS Revenue_Per_Customer
FROM dbo.Multi_touch_market_attribution;