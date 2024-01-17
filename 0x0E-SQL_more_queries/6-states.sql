-- creata a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use this particular database 
USE hbtn_0d_usa;
-- create a table in the above db
CREATE TABLE IF NOT EXISTS states 
(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
