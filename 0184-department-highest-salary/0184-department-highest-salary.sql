/* Write your T-SQL query statement below */
-- select name as Employee, salary, row_number() over (PARTITION by departmentId order by salary desc) as rankofdept, name as Department
-- from Employee 
-- where Employee.departmentId=Department.id

with subquery as (

select e.name,e.salary,d.name as deptname ,rank() over (PARTITION by departmentId order by salary desc) as rankofdept
from Employee e 
left join Department d on d.id=e.departmentId
)

select  deptname as Department, name as Employee, Salary
from subquery 
where rankofdept =1

-- select e.name,e.salary,d.name ,row_number() over (PARTITION by departmentId order by salary desc) as rankofdept
-- from Employee e 
-- left join Department d on d.id=e.departmentId




