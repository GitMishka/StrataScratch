with ranks as (select  
rank() over (partition by product_category order by total_sales desc) as rnk
, product_category
, market_place
, total_sales
, seller_id
, month 
from sales_data)
#select * from ranks
SELECT
    product_category,
    seller_id,
    total_sales,
    month
FROM ranks
where month = '2024-01' and rnk <=3
ORDER BY
    product_category, rnk;