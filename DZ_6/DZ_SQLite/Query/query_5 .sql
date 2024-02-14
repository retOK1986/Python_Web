SELECT sb.name
FROM subjects sb
WHERE sb.teacher_id = ?;  -- Підставте ID викладача