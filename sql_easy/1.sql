-- You are provided with a transactional dataset from Amazon that contains detailed information about sales across different products and marketplaces. Your task is to list the top 3 sellers in each product category for January.

-- The output should contain 'seller_id' , 'total_sales' ,'product_category' , 'market_place', and 'month'.

with ranked_sales as (
    select 
        *
        ,DENSE_RANK() OVER (PARTITION by product_category ORDER BY total_sales desc) as sales_rank
    from sales_data
    WHERE MONTH = '2024-01'
)

SELECT
    seller_id,
    total_sales,
    product_category,
    market_place,
    month

FROM
    ranked_sales
WHERE
    sales_rank <= 3
ORDER BY
    product_category, sales_rank;