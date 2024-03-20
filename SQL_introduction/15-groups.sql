-- List number of records with the same score in second_table, sorted by count (descending).
SELECT `score`, COUNT(`score`) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
