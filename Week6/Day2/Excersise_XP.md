SELECT * FROM items WHERE item_price BETWEEN 0 AND 1000;

SELECT * FROM customers WHERE customer_id BETWEEN 1 AND 3 AND customer_first_name BETWEEN 'a' AND 'z';

SELECT DISTINCT customer_second_name FROM customers ORDER BY customer_second_name DESC;



SELECT * FROM customer
SELECT * FROM film


SELECT first_name, last_name FROM customer AS full_name;

SELECT DISTINCT create_date FROM customer

SELECT email, last_name, first_name FROM customer GROUP BY first_name, last_name, email

SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC 

SELECT address, phone, district FROM address WHERE district = 'Texas'

SELECT * FROM film WHERE film_id BETWEEN 15 AND 20

SELECT * FROM film WHERE title in ('Apocalypse Flamingos')

SELECT * FROM film WHERE title ILIKE 'ap%'

SELECT * FROM film WHERE rental_rate <= 1 LIMIT 10

SELECT customer.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM customer
INNER JOIN payment
ON payment.customer_id = customer.customer_id 

SELECT * FROM film WHERE film_id not in (SELECT film_id FROM inventory)

SELECT city.city, country.country_id, country.country
FROM city
INNER JOIN country
ON city.country_id = country.country_id 
