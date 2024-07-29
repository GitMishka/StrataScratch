SELECT product_category,
     COUNT(DISTINCT transaction_id) AS transactions,
     SUM(sales) AS sales
FROM wfm_transactions AS tr
INNER JOIN wfm_products AS pr ON pr.product_id = tr.product_id
WHERE YEAR(transaction_date) = 2017
GROUP BY product_category
ORDER BY SUM(sales) DESC