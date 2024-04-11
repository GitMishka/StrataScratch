WITH OrderedPurchases AS (
    SELECT
        user_id,
        created_at,
        LAG(created_at) OVER (PARTITION BY user_id ORDER BY created_at) AS previous_purchase_date
    FROM
        amazon_transactions
),
ReturningActiveUsers AS (
    SELECT
        user_id
    FROM
        OrderedPurchases
    WHERE
        previous_purchase_date IS NOT NULL
        AND DATEDIFF(day, previous_purchase_date, created_at) <= 7
    GROUP BY
        user_id
)
SELECT
    user_id
FROM
    ReturningActiveUsers;
