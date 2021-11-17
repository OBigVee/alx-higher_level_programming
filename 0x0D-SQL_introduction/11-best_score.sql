-- script lists all the records with a score >=10 in the second_table table of the database hbtn_0c_0 in your MySQL server

SELECT score,name FROM second_table WHERE  score >= 10 ORDER BY score DESC;
