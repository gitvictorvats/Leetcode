# Write your MySQL query statement below

with manager_table as (

select managerid,count(case when name then 1 else 0 end) as count_reportee
from employee
group by managerid
)

select t2.name as name
from manager_table t1
join Employee t2
on t1.managerid=t2.id
where count_reportee>=5 and t1.managerid is not null