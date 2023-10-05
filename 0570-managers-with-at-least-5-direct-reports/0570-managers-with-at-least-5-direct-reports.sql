# Write your MySQL query statement below

# with subQuery as (

# select E2.name as Manager_name,E1.managerId as Manager ,E1.id as reportee
# from Employee E1
# LEFT JOIN Employee E2
# ON E1.managerId=E2.id

# )



SELECT E2.name
FROM Employee E1
 JOIN Employee E2 ON E1.managerId = E2.id
GROUP BY E2.id
HAVING COUNT(E1.id) >= 5;













