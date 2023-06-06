-- script lists all cities contained in db htbn_0d_usa

SELECT cities.id AS 'id', cities.name AS 'name', states.name AS 'name'
  FROM cities AS c
       INNER JOIN states AS s
       ON c.state_id = s.id
 ORDER BY c.id ASC;