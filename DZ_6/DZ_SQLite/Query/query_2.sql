SELECT s.fullname, AVG(g.grade) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = ?  -- Підставте ID предмета
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;