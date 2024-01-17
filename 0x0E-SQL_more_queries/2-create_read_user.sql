-- create a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- create user to access the database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
-- provide only select previlege to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
