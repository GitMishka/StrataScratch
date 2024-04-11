select 

pr.title,
ceiling(pr.budget * 1.0 / count(emp_id))  as bud_per_emp

from ms_projects pr
join ms_emp_projects emp on pr.id = emp.project_id
group by title, budget
order by bud_per_emp desc
