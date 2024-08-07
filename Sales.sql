CREATE DATABASE Sales;
Use Sales;
CREATE TABLE Customer_details(customer_code VARCHAR(255), customer_name VARCHAR(255),customer_type VARCHAR(255));
insert into Customer_details(customer_code,customer_name,customer_type) VALUES('Cus012','interation Store','Brick & Mortar'),('Cus013','Unity Store','Brick & Mortar'),('Cus014','forward Store','Brick & Mortar'),('Cus015','Electricalbea Store','Brick & Mortar'),('Cus016','Logic Store','Brick & Mortar'),('Cus017','Epic Store','Brick & Mortar'),('Cus018','Electricalslance Store','Brick & Mortar'),('Cus019','Electricalsopedia Store','Brick & Mortar'),
('Cus020','Nixon','E-Commerce'),('Cus021','Modular','E-Commerce'),('Cus022','Electricalslytical','E-Commerce'),('Cus023','Sound','E-Commerce'),('Cus024','Power','E-Commerce'),('Cus025','Path','E-Commerce'),('Cus026','Insight','E-Commerce'),('Cus027','Control','E-Commerce'),('Cus028','Sage','E-Commerce'),('Cus029','Electrivalsocity','E-Commerce'),('Cus030','Synthetic','E-Commerce');  

SELECT * FROM Customer_details WHERE customer_type='E-Commerce'; 

