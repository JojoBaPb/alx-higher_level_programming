-- Lists all records in the table second_table with a score >= 10 in my MySQL server.
-- Records are ordered by score from top to bottom.
SELECT `score`, `name` FROM `second_table` WHERE `score` >= 10  ORDER BY `score` DESC;
