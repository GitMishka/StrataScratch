select 
#extract(week from week),
week,
sum(quantity) from orders_analysis
where quarter(week) = 1 and year(week) = 2023
group by week
