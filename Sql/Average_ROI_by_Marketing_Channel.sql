SELECT
    Channel,
    ROUND(AVG(ROI),2) AS Average_ROI
FROM dbo.Multi_touch_market_attribution
GROUP BY Channel
ORDER BY Average_ROI DESC
