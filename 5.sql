-- Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. Output just the absolute difference in salaries.

select 
(select max(salary) from db_employee e 
join db_dept d
on e.department_id = d.id
where department = 'marketing') 
-
(select max(salary) from db_employee e 
join db_dept d
on e.department_id = d.id
where department = 'engineering') b


or 


WITH eng AS (
    SELECT MAX(emp.salary) AS max_salary
    FROM db_employee emp
    JOIN db_dept dept ON dept.id = emp.department_id
    WHERE dept.department = 'engineering'
), 
mark AS (
    SELECT MAX(emp.salary) AS max_salary
    FROM db_employee emp
    JOIN db_dept dept ON dept.id = emp.department_id
    WHERE dept.department = 'marketing'
)

SELECT ABS((SELECT max_salary FROM eng) - (SELECT max_salary FROM mark)) AS salary_difference;