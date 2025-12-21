-- Creates the table force_name on your MySQL server
-- id: INT
-- name: VARCHAR(256), cannot be NULL
-- If the table already exists, the script will not fail
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
