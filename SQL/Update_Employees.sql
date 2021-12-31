CREATE TABLE update_employee
( 
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  update_date date NOT NULL,
  employee_id int,
  address char(200),
  email char(50),
  phone char(13),
  salary int
);