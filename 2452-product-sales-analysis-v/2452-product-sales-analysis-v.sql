# Write your MySQL query statement below

select user_id, sum(price*quantity) as spending
from Sales s
left join Product p
on s.product_id=p.product_id
group by user_id
order by sum(price*quantity) desc,user_id asc
