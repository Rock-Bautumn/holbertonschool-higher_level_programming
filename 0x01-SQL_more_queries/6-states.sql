-- Write a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.

-- Make the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

--Make the table
CREATE TABLE IF NOT EXISTS states (id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256));
