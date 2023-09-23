# Write your MySQL query statement below
delete  T2
from Person T1
join Person T2
on T1.email=T2.email
where T1.id <T2.id;
