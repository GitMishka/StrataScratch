select title,budget / count(emp_id) from ms_projects pr
join ms_emp_projects emp on pr.id = emp.project_id
group by title,budget
order by budget desc
