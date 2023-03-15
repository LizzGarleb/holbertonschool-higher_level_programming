-- Script that lists all Comedy shows in the database
SELECT tv_shows.title FROM tv_show_genres RIGHT JOIN tv_shows ON show_id = tv_shows.id RIGHT JOIN tv_genres ON genre_id = tv_genres.id WHERE name = "Comedy" ORDER BY tv_shows.title;
