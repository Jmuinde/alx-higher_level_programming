-- script to list all the shows in a database 

select tv_shows.title, tv_show_genres.genre_id
from tv_shows
inner join tv_show_genres
on tv_shows.id = tv_show_genres.show_id
order by title, genre_id;
