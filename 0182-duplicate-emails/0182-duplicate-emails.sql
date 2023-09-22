SELECT DISTINCT A.email as Email 
FROM Person A JOIN Person B
ON A.email = B.email
WHERE A.id <> B.id