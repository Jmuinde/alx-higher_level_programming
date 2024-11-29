--
select tv_shows.title, tv_show_genres.genre_id
from tv_shows
left join tv_show_genres
on tv_shows.id = tv_show_genres.show_id
where genre_id is Null 
order by title, genre_id;
