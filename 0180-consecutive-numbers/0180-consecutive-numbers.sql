# Write your MySQL query statement below

-- select distinct t1.num as ConsecutiveNums
-- from logs t1
-- left join logs t2
-- on t1.id=t2.id+1
-- left join logs t3
-- on t2.id=t3.id+1
-- where t1.num=t2.num and t2.num=t3.num   

with cte as (
select 
id,num,
lead(id,1) over(order by id) as next_id,
lead(num,1) over(order by id) as next_num,
lag(id,1) over (order by id)as  prev_id,
lag(num,1) over (order by id) as  prev_num
from Logs
)

select distinct num as ConsecutiveNums
from cte
where num=next_num and num=prev_num
