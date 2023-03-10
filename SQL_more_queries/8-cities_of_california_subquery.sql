-- Script that lists all the cities of Cali that can be found
SELECT id, name FROM cities WHERE state_id.name=California ORDER BY cities.id;
