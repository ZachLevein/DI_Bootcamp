-- Database: public

-- DROP DATABASE public;

CREATE DATABASE public
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
CREATE TABLE items(
	item_id SERIAL PRIMARY KEY,
	item_name VARCHAR (50) NOT NULL,
	item_price SMALLINT NOT NULL
)
 
INSERT INTO items(item_name, item_price)
	VALUES('Small Desk', 100)

INSERT INTO items(item_name, item_price)
	VALUES('Large Desk', 300)
	
INSERT INTO items(item_name, item_price)
	VALUES('Fan', 80)
	
CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	customer_first_name VARCHAR (50) NOT NULL,
	customer_second_name VARCHAR (50) NOT NULL
)
 INSERT INTO customers(customer_first_name, customer_second_name)
 	VALUES ('Greg', 'Jones')
 INSERT INTO customers(customer_first_name, customer_second_name)
 	VALUES ('Sandra', 'Jones')
 INSERT INTO customers(customer_first_name, customer_second_name)
 	VALUES ('Scott', 'Scott')
 INSERT INTO customers(customer_first_name, customer_second_name)
 	VALUES ('Trevor', 'Green')
 INSERT INTO customers(customer_first_name, customer_second_name)
 	VALUES ('Mealnie', 'Johnson')

SELECT * FROM items
SELECT * FROM items WHERE item_price > 80
SELECT * FROM items WHERE item_price <= 300

SELECT * FROM customers
SELECT * FROM customers WHERE customer_second_name = 'Smith'
SELECT * FROM customers WHERE customer_second_name = 'Jones'
SELECT * FROM customers WHERE customer_second_name != 'Scott'

