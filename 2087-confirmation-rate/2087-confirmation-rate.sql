# Write your MySQL query statement below
# select s.user_id,(action)
# from Signups s
# left join Confirmations c
# ON s.user_id=c.user_id

#Group By s.user_id


# select * #s.user_id,
# from Signups s
# natural left join Confirmations c

SELECT 
    user_id,
    ROUND(AVG(IF(action = 'confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups 
LEFT JOIN Confirmations USING (user_id)
GROUP BY user_id

