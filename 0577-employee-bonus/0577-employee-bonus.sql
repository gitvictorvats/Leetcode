# Write your MySQL query statement below

select  name,bonus
from Employee T1
Left JOIN Bonus T2
ON T1.empId=T2.empId
where bonus<1000 or bonus is null

