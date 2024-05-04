WITH LastMonthSales AS (
    SELECT
        product_id,
        product_group,
        sale_amount,
        date,
        seller_id
    FROM
        Sales
    WHERE
        date >= DATE_TRUNC('month', CURRENT_DATE) - INTERVAL '1 month'
        AND date < DATE_TRUNC('month', CURRENT_DATE)
),
GroupSales AS (
    SELECT
        product_group,
        SUM(sale_amount) AS total_sales
    FROM
        LastMonthSales
    GROUP BY
        product_group
    ORDER BY
        total_sales DESC
    LIMIT 10
),
TopSellers AS (
    SELECT
        s.product_group,
        s.seller_id,
        SUM(s.sale_amount) AS seller_sales
    FROM
        LastMonthSales s
    INNER JOIN
        GroupSales g ON s.product_group = g.product_group
    GROUP BY
        s.product_group, s.seller_id
    ORDER BY
        s.product_group, seller_sales DESC
)
SELECT
    product_group,
    seller_id,
    seller_sales
FROM
    TopSellers
QUALIFY
    ROW_NUMBER() OVER(PARTITION BY product_group ORDER BY seller_sales DESC) <= 100;
