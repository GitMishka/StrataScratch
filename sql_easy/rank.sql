with ranks as (select  
*,
DENSE_RANK() over (partition by product_category order by total_sales desc) as rnk
from sales_data where month = '2024-01') 


SELECT
    product_category,
    seller_id,
    total_sales,
    month
FROM ranks
where rnk <=3
ORDER BY
    product_category, rnk;