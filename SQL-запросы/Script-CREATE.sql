CREATE TABLE IF NOT EXISTS genre (
	id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	Name varchar(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(60) NOT NULL,
	year_album integer NOT NULL	
);

CREATE TABLE IF NOT EXISTS collection (
	id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(60) NOT NULL,
	year_collection integer NOT NULL	
);

CREATE TABLE IF NOT EXISTS track (
	id integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	Name varchar(60) NOT NULL,
	Time_track time NOT NULL,
	Album integer NOT NULL REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS Executor (
	id serial PRIMARY KEY,
	name varchar(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS genre_executor (
	genre_id integer REFERENCES genre(id),
	executor_id integer REFERENCES executor(id),
	CONSTRAINT PK_genre PRIMARY KEY (genre_id,
executor_id)
);

CREATE TABLE IF NOT EXISTS album_executor (
	album_id integer REFERENCES album(id),
	executor_id integer REFERENCES executor(id),
	CONSTRAINT PK_album PRIMARY KEY (album_id,
executor_id)
);

CREATE TABLE IF NOT EXISTS collection_track (
	collection_id integer REFERENCES collection(id),
	track_id integer REFERENCES track(id),
	CONSTRAINT PK_collection PRIMARY KEY (collection_id,
Track_id)
);