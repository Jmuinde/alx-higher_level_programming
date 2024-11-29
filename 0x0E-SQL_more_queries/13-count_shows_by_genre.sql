--
select name as genre, count(name) as number_of_shows
from tv_genres
group by name
order by number_of_shows desc;
