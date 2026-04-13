create database if not exists satartsql;
use startsql;

CREATE table users(
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
    gender ENUM('Male','Female', 'Others'),
	date_of_birth date,
    salary decimal (10,30),
    created_at timestamp default current_timestamp
);
