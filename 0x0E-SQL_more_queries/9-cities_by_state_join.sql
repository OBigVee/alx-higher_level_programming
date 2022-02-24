-- Script lists all cities contained in the database hbtn_0d_usa.
SELECT cities.id, cities.name, states.name FROM states INNER JOIN ON state_id = cities.state_id;
