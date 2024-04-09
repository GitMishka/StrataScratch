with cte1  as (
select  worker_title, salary, rank() over (order by salary desc) as rnk from worker w
join title t on w.worker_id = t.worker_ref_id)

select worker_title from cte1 where rnk = 1 order by worker_title asc
