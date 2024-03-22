-- List genres and their show counts
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS num_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY genre
ORDER BY num_shows DESC;
