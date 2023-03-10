-- Script that list all shows
SELECT tv_shows.title, tv_shows_genres.genre_id FROM title JOIN genre_id ON tv_shows.title=tv_shows_genres.genre_id ORDER BY tv_shows.title, tv_shows_genres.genre_id;
