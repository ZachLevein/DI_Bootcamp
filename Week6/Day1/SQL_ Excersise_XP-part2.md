-- Database: Bootcamp

-- DROP DATABASE "Bootcamp";

CREATE DATABASE "Bootcamp"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE students(
	student_id SERIAL PRIMARY KEY,
	first_name VARCHAR (50) NOT NULL,
	last_name VARCHAR (100) NOT NULL,
	age DATE NOT NULL
	)
	
INSERT INTO students (first_name, last_name, age)
VALUES
('Marc','Benichou','02/11/1998'),
('Yoan', 'Cohen', '03/12/2010'),
('Lea', 'Benichou','11/07/1987'),
('Amelia', 'Dux', '07/04/1996'),
('David', 'Grez', '12/06/2003'),
('Omer', 'Simpson', '03/10/1980');

SELECT * FROM students

SELECT * FROM students WHERE student_id = 2

SELECT * FROM students WHERE last_name = 'Benichou' AND first_name = 'Marc'

SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc'

SELECT * FROM students WHERE first_name LIKE '%a%' ;

SELECT * FROM students WHERE first_name ILIKE 'a%' ;

SELECT * FROM students WHERE student_id = 1 OR student_id = 3