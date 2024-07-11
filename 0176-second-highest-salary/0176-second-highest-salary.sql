SELECT MIN(salary) as SecondHighestSalary FROM 
(
    SELECT distinct TOP 2 salary
    FROM Employee
    ORDER BY salary DESC
) AS x
WHERE (SELECT COUNT(DISTINCT salary) FROM Employee) > 1;


