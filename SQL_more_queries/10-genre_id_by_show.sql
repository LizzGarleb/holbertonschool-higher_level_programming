-- Script that list all shows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows JOIN tv_shows ON tv_shows_genres ORDER BY tv_shows.title, tv_shows_genres.genre_id;
