-- Script that list all records with a score >= 10 in a table
SELECT score, name FROM second_table ORDER BY score DESC HAVING score>=10;
