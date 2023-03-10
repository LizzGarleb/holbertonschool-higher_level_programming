-- Script that lists all the cities of Cali that can be found
SELECT id, name FROM cities WHERE state_id=1 ORDER BY cities.id;
