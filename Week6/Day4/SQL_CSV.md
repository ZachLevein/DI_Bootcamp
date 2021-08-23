-- Database: MCA

-- DROP DATABASE "MCA";

CREATE DATABASE "MCA"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

CREATE TABLE business(
	business_id SERIAL PRIMARY KEY,
    biz_name VARCHAR (100) NOT NULL,
	created DATE NOT NULL, 
	open_deals INT,
	won_deals INT,
	statee VARCHAR, 
	full_address TEXT, 
	EIN CHARACTER VARYING,
	business_start_date CHARACTER VARYING
);

DROP TABLE business

COPY business(biz_name, created, open_deals, won_deals, statee, full_address, EIN, business_start_date )
FROM 'C:\Users\Public\org.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM BUSINESS;

CREATE TABLE people(
	person_id SERIAL PRIMARY KEY,
    person_name VARCHAR (100) NOT NULL,
	phone VARCHAR,
	phone_2 VARCHAR,
	person_created DATE NOT NULL, 
	email CHARACTER VARYING,
	account CHARACTER VARYING,
	social_security_number VARCHAR, 
	date_of_birth CHARACTER VARYING, 
	time_zone CHARACTER VARYING
);

drop table people 

COPY people(person_name, phone, phone_2, person_created, email, account, social_security_number, date_of_birth, time_zone)
FROM 'C:\Users\Public\peep.csv'
DELIMITER ',' CSV HEADER;


SELECT * business.biz_name
FROM business
WHERE business.business_id = ( people.person_id
							 FROM people)
							 
SELECT people.person_name, business.biz_name, business.open_deals
FROM PEOPLE, business
WHERE people.person_id = business.business_id AND business.open_deals >= 1
LIMIT(25)

SELECT * FROM business WHERE business_id = 52

CREATE TABLE deals(
	deal_id SERIAL PRIMARY KEY ,
    amount VARCHAR (100),
	deal_created VARCHAR, 
	deal_closed CHARACTER VARYING,
	stage VARCHAR (50), 
	pipeline VARCHAR (50),
	biz_name VARCHAR (100)
);

DROP TABLE deals

COPY deals(biz_name, amount, deal_created, deal_closed, stage, pipeline)
FROM 'C:\Users\Public\deals.csv'
DELIMITER ',' CSV HEADER;

SELECT * FROM deals

SELECT business.business_id, deals.biz_name, deals.amount, deals.pipeline, deals.stage, deals.deal_created
INTO new_table
FROM business
INNER JOIN deals
ON business.biz_name = deals.biz_name

drop table new_table

select * from new_table
						  
	