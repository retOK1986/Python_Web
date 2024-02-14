SELECT gr.name AS group_name, AVG(g.grade) AS average_grade
FROM groups gr
JOIN students s ON gr.id = s.group_id
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = ?  -- Підставте ID предмета
GROUP BY gr.id;