# Write your MySQL query statement below

select product_name, sum(unit) as unit
from Orders
left join Products
using (product_id)
WHERE EXTRACT(YEAR FROM order_date) = 2020 AND EXTRACT(MONTH FROM order_date) = 2
group by product_id
having sum(unit) >=100

