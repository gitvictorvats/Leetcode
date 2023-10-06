# Write your MySQL query statement below

WITH ConfirmationCounts AS (
    SELECT 
        user_id,
        SUM(IF(action = 'confirmed', 1, 0)) AS confirmed_count,
        COUNT(action) AS total_count
    FROM Signups 
    LEFT JOIN Confirmations USING (user_id)
    GROUP BY user_id
)

SELECT
    user_id,
    COALESCE(ROUND(confirmed_count * 1.0 / total_count, 2), 0.00) AS confirmation_rate
FROM ConfirmationCounts;





