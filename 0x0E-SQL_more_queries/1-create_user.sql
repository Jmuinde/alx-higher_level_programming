-- create a user with all the previleges

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'User_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

