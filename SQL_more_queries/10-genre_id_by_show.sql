-- import the database dump from hbtn_0d_tvshows to your MySQL server.
SELECT tv_shows.title, tv.show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv.shows.id = tv_show_genres.show_id
ORDER BY tv.shows.title ASC, tv_show_genres.genre_id ASC;