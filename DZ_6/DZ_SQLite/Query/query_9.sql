SELECT DISTINCT sb.name
FROM subjects sb
JOIN grades g ON sb.id = g.subject_id
JOIN students s ON g.student_id = s.id
WHERE s.id = ?;  -- Підставте ID студента
