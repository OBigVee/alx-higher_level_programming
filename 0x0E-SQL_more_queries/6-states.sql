--script creates database htbn_0d_usa and table states 

CREATE DATABASE IF NOT EXISTS htbn_0d_usa;
CREATE TABLE IF NOT EXISTS states
    (
        id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY(id),
        name VARCHAR(256) NOT NULL
    );
