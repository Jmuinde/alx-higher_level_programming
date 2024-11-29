-- script to create a database and add tables 

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa; 
use hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(id int  AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256));
