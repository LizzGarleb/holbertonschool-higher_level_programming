-- Script that list all cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = state_id ORDER BY cities.id;
