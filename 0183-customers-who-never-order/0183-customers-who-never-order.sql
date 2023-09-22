# Write your MySQL query statement below
SELECT name as Customers
from Customers
LEFT Join Orders
ON Customers.id=Orders.customerId
where Orders.id is  NULL
