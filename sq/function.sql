use  startersql;
--  update users set salary = 70000  where id =5;
-- UPDATE users SET salary = salary - 10000 WHERE id > 0 and salary < 66000 ;
-- delete from users where id = 2 ;
-- alter table users add constraint dob check(date_of_birth > '1920-01-01'); 
-- count fun...........""
select count(*) from users where gender = 'male';
select min(salary) as  min_salary , max(salary) as max_salary from users;
select avg (salary) as avg_salary from users;
select  gender , sum(salary) as avg_salary from users group by gender;
select id,gender, name, length(name) as name_len from users;

select id,gender, lower(name) as lower_name ,concat((name) , "455656") as username, now() as time , year(date_of_birth) as date_of_year, length(name) as name_len from users;

-- select * from users;

