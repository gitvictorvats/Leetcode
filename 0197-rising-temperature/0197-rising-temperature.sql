# Write your MySQL query statement below
select t1.id#,t1.recordDate,t1.temperature,t2.id,t2.recordDate,t2.temperature
from Weather t1
join Weather t2
on DATEDIFF(t1.recordDate, t2.recordDate) = 1
where t1.temperature>t2.temperature
