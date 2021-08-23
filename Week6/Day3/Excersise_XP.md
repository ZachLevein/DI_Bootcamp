SELECT title FROM film AS language_name
UNION 

SELECT name FROM language;

SELECT * FROM film WHERE language_id = 0 

SELECT * FROM language

CREATE TABLE new_film(
	new_film_id SERIAL PRIMARY KEY NOT NULL,
	title VARCHAR (50) NOT NULL
	)
INSERT INTO new_film (title)
VALUES
('The Godfather'),
('Saw'),
('I shot the sherrif')

select * from new_film
	
CREATE TABLE customer_review(
	review_id SERIAL PRIMARY KEY,
	new_film_id int,
	language_id int,
	FOREIGN KEY (new_film_id) REFERENCES new_film(new_film_id),
	FOREIGN KEY (language_id) REFERENCES language(language_id),
	review_text VARCHAR (75), 
	last_update DATE NOT NULL

	)
 DROP TABLE customer_review

INSERT INTO customer_review(review_text)
VALUES
('MOVIE FCKIN SUCKED BALLS')

SELECT new_film.title, customer_review.review_text
FROM new_film 
INNER JOIN customer_review
ON new_film.new_film_id = customer_review.new_film_id