-- create new user and set password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
-- grant all previleges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
