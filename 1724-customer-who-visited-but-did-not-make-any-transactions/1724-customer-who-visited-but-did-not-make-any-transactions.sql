# Write your MySQL query statement below

With subQuery as
(
select Visits.visit_id,Visits.customer_id,Transactions.transaction_id
from Visits
Left Join Transactions
ON Visits.visit_id=Transactions.visit_id
)


SELECT customer_id, COUNT(*) as count_no_trans
FROM subQuery
WHERE transaction_id IS NULL
GROUP BY customer_id;

# select customer_id, COUNT(transaction_id) as count_no_trans
# from subQuery
# where transaction_id is null
# GROUP BY customer_id;







