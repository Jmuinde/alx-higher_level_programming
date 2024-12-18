-- create a database, add a user and grant them select privelleges.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2. * TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;