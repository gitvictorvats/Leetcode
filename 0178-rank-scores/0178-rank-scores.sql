
with cte as (
select id,score, dense_rank() over (order by score desc) as ranked_score
from scores
)

select score ,ranked_score as 'rank'
from cte
order by score desc


