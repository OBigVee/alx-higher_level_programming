--script that lists all records of the table second_table
-- of the database hbtn_0c_0 in MySQL server
SELECT score, name FROm second_table WHERE name IS NOT NULL ORDER BY score DESC;