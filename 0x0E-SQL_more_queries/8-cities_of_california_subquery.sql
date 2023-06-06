-- lists all the cities of `California` that can be found in the
-- database `hbtn_0d_usa` provided that:
-- states ++++++++++++++++++
-- id  name
-- 1   California
-- 2   Arizona
-- 3   Texas
-- 4   Utah
-- cities ++++++++++++++++++
-- id  state_id    name
-- 1   1   San Francisco
-- 2   1   San Jose
-- 4   2   Page
-- 6   3   Paris
-- 7   3   Houston
-- 8   3   Dallas
--
-- + The states table contains only one record where
--   `name` = `California`
-- + Results must be sorted in ascending order by `cities.id`
-- + You are not allowed to use the `JOIN` keyword

SELECT id, name
  FROM cities
 WHERE state_id = ( SELECT id
		      FROM states
		     WHERE name = 'California')
 ORDER BY id ASC;