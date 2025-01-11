# Write your MySQL query statement below

with cte as (
select 
id,name,salary,departmentID,

rank() over (partition by departmentID order by salary desc ) as rank_salary
from employee

)

select t2.name as Department,t1.name as Employee,salary
from cte t1
left join department t2 on t1.departmentId=t2.id
where rank_salary=1


