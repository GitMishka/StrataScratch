with m_salaries as (select id, max(salary) as current_salary from ms_employee_salary group by id)

select  
m.id, 
first_name, 
last_name, 
department_id, 
current_salary 
FROM ms_employee_salary e
INNER JOIN m_salaries m ON e.id = m.id AND e.salary = m.current_salary ORDER BY e.id ASC;