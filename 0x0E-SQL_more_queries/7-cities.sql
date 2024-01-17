-- creata a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use this particular database 
USE hbtn_0d_usa;
-- create a table in the above db
CREATE TABLE IF NOT EXISTS cities 
(id INT PRIMARY KEY AUTO_INCREMENT, 
state_id INT NOT NULL, 
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id));
