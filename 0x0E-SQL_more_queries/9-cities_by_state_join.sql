-- joning 
select cities.id, cities.name, states.name 
from states
inner join cities
on states.id = cities.state_id;            
