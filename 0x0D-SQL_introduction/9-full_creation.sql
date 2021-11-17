-- script creates a tbale second_tabel in the database hbtn_0c_0 in your MySQL server and add multiples rows
CREATE TABLE IF NOT EXISTS second_table(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256), score INT);
UPDATE second_table
SET name = "John", score = 10 WHERE id = 1
SET name = "Alex", score = 3 wHERE id = 2
SET name = "Bob", score = 14 WHERE id = 3
SET name = "George", score = 8 WHERE id = 8;
