INSERT
	INTO
	collection (name,
	year_collection)
VALUES('Only Hit', '2021'),
('TOP20', '2020'),
('TOP50', '2018'),
('HIT50', '2019'),
('The Best June', '2017'),
('Collection 2016', '2016'),
('TOP100', '2010'),
('TOP-HIT', '2022');

INSERT
	INTO
	album (name,
	year_album)
VALUES('Vinyl #1', '2020'),
('Joanne', '2016'),
('One More Light', '2017'),
('Dont Cry', '1994'),
('Rare', '2018'),
('Ghetto in the Sky', '2017'),
('Live At The Paramount', '2019'),
('Human After All', '2005');

INSERT
	INTO
	track (name,
	time_track,
	album)
VALUES('Life', '00:03:07', '1'),
('Credo', '00:03:04', '1'),
('Angel Down', '00:04:04', '2'), 
('Sorry for Now', '00:03:16', '3'),
('Invisible', '00:05:00', '3'),
('Goodbye', '00:02:04', '4'), 
('Celebrate', '00:03:30', '4'),
('My Baby', '00:03:55', '5'),
('Bump Dat', '00:04:01', '5'), 
('Dope in the House', '00:02:11', '6'),
('A Rough Day', '00:02:26', '6'),
('Drain You', '00:03:46', '7'), 
('About A Girl', '00:03:13', '7'),
('Make Love', '00:04:49', '8'),
('The Brainwasher', '00:04:08', '8'),
('Breed', '00:03:11', '7'),
('Polly', '00:03:03', '7');

INSERT
	INTO
	Executor (name)
VALUES('Linkin park'),
('Savage'),
('50 Cent'),
('2Pac'),
('Lady Gaga'),
('Nirvana'),
('Duft Pank'),
('Zivert');

INSERT
	INTO
	genre (name)
VALUES ('Rock'),
('Rap'),
('Pop'),
('Disco'),
('House');

INSERT
	INTO
	genre_executor
VALUES ('1', '1'),
('4', '2'),
('2', '3'),
('2', '4'),
('3', '5'),
('1', '6'),
('5', '7'),
('3', '8'),
('2', '1');

INSERT
	INTO
	album_executor
VALUES ('1', '8'),
('2', '5'),
('3', '1'),
('4', '2'),
('5', '3'),
('6', '4'),
('7', '6'),
('8', '7');

INSERT
	INTO
	collection_track
VALUES ('1', '3'),
('1', '4'),
('2', '20'),
('2', '6'),
('3', '7'),
('3', '8'),
('4', '9'),
('4', '10'), 
('5', '11'),
('5', '12'),
('6', '13'),
('6', '14'),
('7', '15'),
('7', '16'),
('8', '17'),
('8', '18'), 
('8', '19');
