-- Script that uses a database to list all genres of a show
SELECT tv_genres.name FROM tv_shows JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = Dexter ORDER BY tv_genres.name;
