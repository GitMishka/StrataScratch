-- with m as (SELECT MAX(e.salary) 
-- FROM db_employee e 
-- JOIN db_dept d ON e.department_id = d.id
-- WHERE d.department = 'Marketing')
-- , with e as(SELECT MAX(e.salary) 
-- FROM db_employee e 
-- JOIN db_dept d ON e.department_id = d.id
-- WHERE d.department = 'engineering')

select  (SELECT MAX(e.salary) 
FROM db_employee e 
JOIN db_dept d ON e.department_id = d.id
WHERE d.department = 'Marketing')
-
(SELECT MAX(e.salary) 
FROM db_employee e 
JOIN db_dept d ON e.department_id = d.id
WHERE d.department = 'engineering')