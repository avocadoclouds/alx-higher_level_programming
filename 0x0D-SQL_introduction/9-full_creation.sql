-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
-- second_table description:
-- id INT
-- name VARCHAR(256)
-- score INT
CREATE TABLES IF NOT EXISTS second_tables(id INT, name VARCHAR(256), SCORE INT);-- ADDING ROWS
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (1, "John", 10);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (2, "Alex", 3);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (3, "Bob", 14);
INSERT INTO `second_table` (`id`, `name`, `score`) VALUES (4, "George", 8);
