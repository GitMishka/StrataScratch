with feb  as (select datepart(month, joining_date)  as month, * from worker)
select worker_id,	first_name,	last_name,	salary,	joining_date,	department from feb where worker_id % 2 =1 and month = 2
