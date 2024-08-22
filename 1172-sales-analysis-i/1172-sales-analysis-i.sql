# Write your MySQL query statement below

with cte as (
select seller_id,sum(price) as total_sale_per_seller, dense_rank() over (order by sum(price) desc) as rank_order
from Sales
group by seller_id

)

select seller_id
from cte
where rank_order=1




