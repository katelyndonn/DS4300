CREATE DATABASE TwitterDB;

USE TwitterDB;

CREATE TABLE IF NOT EXISTS Tweet
(   tweet_id INT PRIMARY KEY,
    user_id INT,
    tweet_ts DATETIME,
    tweet_text VARCHAR(140)
);

CREATE TABLE IF NOT EXISTS Follows
(   user_id INT,
    follows_id INT
);

CREATE USER 'T_USER'@'localhost' IDENTIFIED BY 'T_PASS';
GRANT ALL ON TwitterDB.* TO 'T_USER'@'localhost';
flush privileges;
