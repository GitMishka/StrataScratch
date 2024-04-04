select c.id,first_name, sum(total_order_cost) from customers c join orders o on c.id = o.cust_id 
group by c.id,first_name
order by first_name asc