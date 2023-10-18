-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- new value for test
--INSERT INTO second_table (id, name, score) VALUES(5, "Aria", 18);
--INSERT INTO second_table (id, name, score) VALUES(6, "Aria", 12);
--INSERT INTO second_table (id, score) VALUES(7, 14);
--INSERT INTO second_table (id, score) VALUES(8, 8);
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
