-- 8-cities_of_california_subquery.sql
USE hbtn_0d_usa;
SELECT id, name FROM cities WHERE cities.id = (
	SELECT states.id FROM states
	WHERE states.name = 'California'
)
ORDER BY cities.id;
