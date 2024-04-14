select i.product_name, count(t.transaction_id) from excel_sql_inventory_data i
join excel_sql_transaction_data t on t.product_id = i.product_id where t.transaction_id is not null
group by i.product_name
order by 2 desc