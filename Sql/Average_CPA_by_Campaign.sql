SELECT
    Campaign,
    ROUND(AVG(CPA_USD),2) AS Average_CPA
FROM dbo.Multi_touch_market_attribution
GROUP BY Campaign
ORDER BY Average_CPA ASC