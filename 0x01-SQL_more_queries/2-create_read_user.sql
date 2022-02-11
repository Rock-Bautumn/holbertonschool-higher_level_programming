-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2. 

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user
CREATE USER IF NOT EXISTS `user_0d_2`@'localhost' IDENTIFIED BY 'hbtn_0d_2_pwd';

-- Set user permissions
GRANT SELECT ON *.hbtn_0d_2 TO `user_0d_2`@'localhost';
