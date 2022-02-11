-- Write a script that creates the MySQL server user user_0d_1.

-- Create the user
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';

-- Grant the permissions
GRANT ALL PRIVILEGES ON *.* TO user_0d_1@localhost;
