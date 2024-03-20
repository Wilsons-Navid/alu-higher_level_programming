-- List all records of second_table, excluding empty names, ordered by score (top first).
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
