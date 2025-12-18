-- Never empty --

CREATE TABLE id_not_null (id INT DEFAULT 1, name VARCHAR(256)) 
IF NOT EXISTS id_not_null;
