select * from employee_list;

select 
    first_name,
    last_name
from employee_list
where profession = 'Doctor' and last_name = 'Johnson'

-- Find doctors with the last name of 'Johnson' in the employee list. The output should contain both their first and last names.