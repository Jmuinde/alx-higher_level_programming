-- subqueries 

SELECT id, name From cities
WHERE state_id =(
			select id 
			from states
			where name = 'California'
		)
ORDER BY id DESC;
