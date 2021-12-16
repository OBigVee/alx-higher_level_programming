-- script lists the number of record wih the same score in the table secon_table of the database hbtn_0c_0 in your MySQL server.
SELECT score , COUNT(*)  AS number FROM second_table GROUP BY score ORDER BY number DESC;
