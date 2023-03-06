SELECT
	name,
	year_album
FROM
	album
WHERE
	year_album = 2018;

SELECT
	name,
	time_track
FROM
	track
WHERE
	time_track = (
	SELECT
		max(Time_track)
	FROM
		track);

SELECT
	name
FROM
	track
WHERE
	time_track >= '00:03:30';

SELECT
	name
FROM
	collection
WHERE
	year_collection >= 2018
	AND year_collection <= 2020;

SELECT
	name
FROM
	executor
WHERE
	name NOT LIKE '% %';

SELECT
	name
FROM
	track
WHERE
	lower(name) LIKE '%my%';
