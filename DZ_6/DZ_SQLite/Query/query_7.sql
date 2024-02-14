SELECT s.fullname, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.group_id = ? AND g.subject_id = ?;  -- Підставте ID групи і ID предмета