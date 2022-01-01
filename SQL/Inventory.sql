CREATE TABLE inventory
( 
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  update_date date NOT NULL,
  material_id INT,
  amount float
);