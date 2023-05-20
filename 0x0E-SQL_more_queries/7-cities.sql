--script creates database hbtn_0d_usa and table cities 
-- create db
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--create table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY(id),
    state_id INT NOT NULL FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
    name VARCHAR(256) NOT NULL
);