--total conversions

SELECT
    COUNT(*) AS Total_Conversions
FROM dbo.Multi_touch_market_attribution
WHERE Conversion = 1;