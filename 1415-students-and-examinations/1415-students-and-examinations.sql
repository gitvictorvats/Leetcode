# Write your MySQL query statement below

WITH subQuery AS (
    SELECT student_id, student_name, subject_name
    FROM Students
    CROSS JOIN Subjects
)

SELECT 
    sq.student_id,
    sq.student_name,
    sq.subject_name,
    COUNT(e.subject_name) AS attended_exams
FROM subQuery sq
LEFT JOIN Examinations e ON sq.student_id = e.student_id AND sq.subject_name = e.subject_name
GROUP BY sq.student_id, sq.subject_name
ORDER BY sq.student_id, sq.subject_name;


# with subQuery as

# (

# select student_id,student_name,subject_name
# from Students st
# CROSS JOIN Subjects su

# )

# select sq.student_id,sq.student_name,sq.subject_name,(select count(DISTINCT subject_name) from Examinations Group BY student_id) AS attended_exams
# from subQuery sq
# LEFT JOIN Examinations e
# ON sq.student_id=e.student_id

# GROUP BY student_id,subject_name












