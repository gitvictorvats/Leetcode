# Write your MySQL query statement below
With subQuery AS
(

select T1.machine_id,T1.process_id,T2.timestamp-T1.timestamp AS processing_time
from Activity T1
JOIN Activity T2
ON T1.machine_id =T2.machine_id
where T1.process_id=T2.process_id AND T1.activity_type='start' and T2.activity_type='end'
#Group By(T1.machine_id)

)

select machine_id,round(avg(processing_time),3) as processing_time
from subQuery
Group BY machine_id




