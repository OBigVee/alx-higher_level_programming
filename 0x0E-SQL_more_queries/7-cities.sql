--script creates database hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	PRIMARY KEY (id),
	FOREIGN KEY (state_id) REFERENCES states(id),
	id		INT UNIQUE AUTO_INCREMENT	NOT NULL,
	state_id	INT				NOT NULL,
	name		VARCHAR(256) 			NOT NULL
);