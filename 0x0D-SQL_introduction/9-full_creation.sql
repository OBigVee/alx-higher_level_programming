--script creates a table second_table in the database
-- hbtn_0c_0 in your MySQL server
-- add multiple rows
CREATE TABLE IF NOT EXISTS second_table (id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256), score INT);

INSERT INTO second_table(id, name, score) VALUES(1, "john", 10);
INSERT INTO second_table(id, name, score) VALUES(2, "Alex", 3);
INSERT INTO second_table(id, name, score) VALUES(3, "Bob", 14);
INSERT INTO second_table(id, name, score) VALUES(4, "George", 8);

