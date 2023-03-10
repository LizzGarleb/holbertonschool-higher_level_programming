-- Script that creates a database and a table
CREATE DATABASE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL;
    UNIQUE (id)
)
