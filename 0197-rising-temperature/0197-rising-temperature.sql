# Write your MySQL query statement below

select T2.id
from Weather as T1
JOIN Weather T2
ON DATEDIFF(T2.recordDate,T1.recordDate)=1
where T2.temperature > T1.temperature


