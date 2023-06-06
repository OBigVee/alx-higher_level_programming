-- script lists all cities contained in db htbn_0d_usa
SELECT * FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;