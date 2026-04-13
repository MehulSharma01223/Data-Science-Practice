create database if  not exists Mehul;
use Mehul;
create table mehul_tblr(
id int(100) primary key auto_increment , 
Name varchar(100) not null ,
class varchar(100) not null ,
Email varchar(200) unique not null , 
Moblie_No int(10) unique not null , 
City varchar(100) not null,
Gender enum('Male','Female'),
 Salary decimal(10,2) not null   
) ; 
