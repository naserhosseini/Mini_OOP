CREATE TABLE orders
( 
  id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
  customer_id INT,
  date DATE,
  product INT,
  type INT,
  quantities INT,
  delivery date,
  status BOOLEAN
);