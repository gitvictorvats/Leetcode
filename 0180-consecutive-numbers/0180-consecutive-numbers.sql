-- select t1.id,t1.num,t2.id,t2.num,t3.id,t3.num
-- from Logs t1
-- join logs t2 on t1.id = t2.id-1
-- join logs t3 on t2.id-1 = t3.id-2

-- where t1.num=t2.num and t2.num=t3.num
select distinct t1.num as ConsecutiveNums
from Logs t1
join logs t2 on t1.id = t2.id-1
join logs t3 on t2.id-1 = t3.id-2

where t1.num=t2.num and t2.num=t3.num