-- Create a table with unique IDs


-- Make the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Make the table
CREATE TABLE IF NOT EXISTS states (id INT DEFAULT 1 UNIQUE, name VARCHAR(256), PRIMARY KEY(id));
