-- Script that list all shows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows JOIN tv_shows_genres ON tv_shows.title=tv_shows_genres.genre_id ORDER BY tv_shows.title, tv_shows_genres.genre_id;
