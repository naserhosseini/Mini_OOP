CREATE TABLE orders
( 
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  customer_id INT,
  date DATE,
  product char(10),
  type char(10),
  quantities INT,
  delivery date,
  status BOOLEAN
);