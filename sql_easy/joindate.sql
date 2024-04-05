with date as (SELECT *, DATEPART(month, joining_date) AS JoiningMonth FROM worker)

select * from date where worker_id % 2 = 0 and JoiningMonth = 6
