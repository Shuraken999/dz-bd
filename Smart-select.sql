--Запрос №1
SELECT 
	g.name, COUNT(executor_id)
FROM 
	genre_executor ge	
JOIN genre g ON ge.genre_id = g.id
GROUP BY 
	g.name
ORDER BY 
	COUNT(executor_id);
--Запрос №2
SELECT 
	a.name, COUNT(t.id)
FROM
	track t
JOIN album a ON t.album = a.id
WHERE a.year_album >= 2019 AND a.year_album <= 2020
GROUP BY 
	a.name
ORDER BY 
	COUNT(t.id);
--Запрос #3
SELECT 
	a.name, AVG(t.time_track)
FROM
	track t
JOIN album a ON t.album = a.id
GROUP BY 
	a.name
ORDER BY 
	AVG(t.time_track);
--Запрос №4
SELECT 
	e.name 
FROM 
	executor e 
JOIN album_executor ae  ON ae.executor_id = e.id
JOIN album a ON ae.album_id = a.id
WHERE NOT a.year_album = 2020
GROUP BY e.name;
--Запрос №5
SELECT 
	c.name, COUNT(e.name)   
FROM 
	collection c
JOIN collection_track ct ON ct.collection_id = c.id
JOIN track t ON ct.track_id = t.id
JOIN album a ON t.album = a.id
JOIN album_executor ae ON ae.album_id = a.id
JOIN executor e ON e.id = ae.executor_id
WHERE e.name = 'Zivert' 
GROUP BY c.name;
--Запрос №6
SELECT 
	COUNT(e.name), a.name
FROM 
	album a
JOIN album_executor ae ON ae.album_id = a.id
JOIN executor e ON e.id = ae.executor_id
JOIN genre_executor ge ON ge.executor_id = e.id
GROUP BY a.name
HAVING count(*)>1;
--Запрос №7
SELECT 
	t.name 
FROM 
	track t
JOIN collection_track ct ON ct.track_id = t.id
JOIN collection c ON c.id = ct.collection_id
WHERE ct.collection_id IS NULL;
--Запрос №8
SELECT 
	e.name, min(t.time_track)
FROM 
	executor e
JOIN album_executor ae ON  ae.executor_id = e.id 
JOIN album a ON a.id = ae.album_id 
JOIN track t ON t.album = a.id 
WHERE t.time_track = (SELECT min(time_track) FROM track )
GROUP BY e.name;
--Запрос №9
SELECT 
	a.name, count(*) 
FROM 
	album a 
JOIN track t ON t.album = a.id 
GROUP BY a.name
ORDER BY count(*) LIMIT 1;

