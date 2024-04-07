SELECT id, first_name, last_name, max(salary) ,department_id 
FROM ms_employee_salary
group by id, first_name, last_name, department_id