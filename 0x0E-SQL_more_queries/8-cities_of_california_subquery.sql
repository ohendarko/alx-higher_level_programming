-- 8-cities_of_california_subquery.sql
USE hbtn_0d_usa;
SELECT * FROM states, cities WHERE name = 'California'
ORDER BY cities.id;
