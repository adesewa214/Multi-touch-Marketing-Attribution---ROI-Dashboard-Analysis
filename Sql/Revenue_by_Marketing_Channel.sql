Select Channel, 
Round(sum(revenue_usd), 2) As
Total_revenue
FRom dbo.Multi_touch_market_attribution
Group by Channel
Order by Total_revenue DESC
