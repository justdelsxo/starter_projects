-- Please check Read.me for creative scenario.

CREATE DATABASE Warehouse;
USE Warehouse;

-- Category - Stores the categories of products the warehouse stocks

CREATE TABLE Category (
Category_id INT AUTO_INCREMENT PRIMARY KEY,
Category_name VARCHAR(50) NOT NULL
);

-- Suppliers - Stores all information on the suppliers the warehouse get their products from

CREATE TABLE Suppliers (
Supplier_id INT AUTO_INCREMENT PRIMARY KEY,
Supplier_name VARCHAR(100) NOT NULL,
Supplier_country VARCHAR(50) NOT NULL,
Email VARCHAR(100) UNIQUE,
Phone_number VARCHAR(20)
);

-- Products - Stores all product information that the warehouse stock

CREATE TABLE Products (
Product_id INT AUTO_INCREMENT PRIMARY KEY,
Product_name VARCHAR(50) NOT NULL,
Category_id INT, FOREIGN KEY (Category_id) REFERENCES Category(Category_id),
Supplier_id INT, FOREIGN KEY (Supplier_id) REFERENCES Suppliers(Supplier_id) ON DELETE CASCADE,
Price_per_unit DECIMAL(6,2) NOT NULL,
Unit ENUM('Kg', 'g', 'Litre', 'ml', 'Pieces') NOT NULL
);

-- Inventory - Stores information on the amount of products currently available at the warehouse

CREATE TABLE Inventory (
Inventory_id INT AUTO_INCREMENT PRIMARY KEY,
Product_id INT, FOREIGN KEY (Product_id) REFERENCES Products(Product_id) ON DELETE CASCADE,
Stock_level INT NOT NULL
);

-- Purchase_orders - Stores all information relating to orders placed 

CREATE TABLE Purchase_orders (
Order_id INT AUTO_INCREMENT PRIMARY KEY,
Product_id INT, FOREIGN KEY (Product_id) REFERENCES Products(Product_id) ON DELETE CASCADE,
Supplier_id INT, FOREIGN KEY (Supplier_id) REFERENCES Suppliers(Supplier_id) ON DELETE CASCADE,
Quantity INT NOT NULL,
Order_date DATE NOT NULL,
Status ENUM('Unfulfilled', 'Shipped', 'Delivered', 'Cancelled', 'Refunded') DEFAULT 'Unfulfilled' NOT NULL -- Setting 'Unfulfilled' as the default order status
);

/*SELECT * 
FROM Products;

SELECT * 
FROM Suppliers;
*/

INSERT INTO Category
(Category_name)
VALUES
('Oils'),
('Butters'),
('Powders'),
('Essences'),
('Solids'),
('Waxes'),
('Foams'),
('Liquids');

SELECT * FROM Category;

INSERT INTO Suppliers
(Supplier_name, Supplier_country, Email, Phone_number)
VALUES
('VelvaGlow Essentials', 'France', 'contact@velvaglow.com', '+33 1 23 45 67 89'),
('PureLeaf Botanics', 'Canada', 'info@pureleaf.ca', '+1 416 555 0198'),
('NaturaFusion Labs', 'Germany', 'sales@naturafusion.de', '+49 30 1234567'),
('Silk & Sage Supplies', 'United Kingdom', NULL, '+44 20 7946 0958'),
('Lushchemy Distributors', 'USA', 'support@lushchemy.com', '+1 212 555 0147'),
('AromaHaven Co.', 'India', 'hello@aromahaven.in', '+91 98765 43210'),
('BareRoots Wholesale', 'Australia', NULL, '+61 2 9876 5432'),
('GlowNest Naturals', 'South Africa', 'team@glownest.co.za', '+27 21 555 1234');

SELECT * FROM Suppliers;

INSERT INTO Products
(Product_name, Category_id, Supplier_id, Price_per_unit, Unit)
VALUES
('Almond oil', 1, 7, 14.99, 'Litre'),
('Jojoba oil', 1, 3, 11.99, 'Litre'),
('Shea butter', 2, 4, 5.49, 'Kg'),
('Turmeric powder', 3, 1, 2.99, 'Kg'),
('Aloe vera powder', 3, 8, 4.79, 'Kg'),
('Cocoa butter', 2, 6, 7.49, 'Kg'),
('Vanilla essence', 4, 2, 1.49, 'Litre'),
('Lemongrass essence', 4, 5, 3.99, 'Litre');

SELECT * FROM Products;

INSERT INTO Inventory
(Product_id, Stock_level)
VALUES
(3, 1),
(8, 279),
(1, 34),
(4, 567),
(7, 18),
(2, 2025),
(5, 0),
(6, 9);

SELECT * FROM Inventory;

INSERT INTO Purchase_orders
(Product_id, Supplier_id, Quantity, Order_date, Status)
VALUES
(8, 5, 35, '2025-05-05', 'Unfulfilled'),
(6, 6, 12, '2025-04-24', 'Cancelled'),
(2, 3, 1000, '2025-05-25', 'Shipped'),
(5, 8, 19, '2025-06-01', 'Delivered'),
(7, 2, 6, '2025-05-20', 'Unfulfilled'),
(4, 1, 234, '2025-04-29', 'Shipped'),
(3, 4, 89, '2025-06-09', 'Refunded'),
(1, 7, 13, '2025-05-12', 'Refunded');

SELECT * FROM Purchase_orders;

-- Products currently out of stock 
SELECT p.Product_name, i.Stock_level
FROM Products AS p
INNER JOIN
Inventory AS i
ON p.product_id = i.product_id
WHERE Stock_level < 1
ORDER BY Stock_level DESC;

-- Procedure created to easily and frequently check low level products in order to keep the inventory stocked for customers to purchase

DELIMITER //

CREATE PROCEDURE Get_low_stock_products()
BEGIN
SELECT p.Product_name, i.Stock_level
FROM Products AS p
INNER JOIN
Inventory AS i
ON p.product_id = i.product_id
WHERE Stock_level < 10
ORDER BY Stock_level DESC;
END //
DELIMITER ;

CALL Get_low_stock_products();

-- List all orders placed in May 2025
SELECT po.Order_id, p.Product_name, po.Quantity, po.Order_date
FROM Products AS p
INNER JOIN Purchase_orders AS po
ON p.Product_id = po.Product_id
WHERE po.Order_date BETWEEN '2025-05-01' AND '2025-05-31'
ORDER BY Order_date DESC;

-- Show the total units ordered and total revenue generated for each product in May 2025
SELECT p.Product_name, po.Order_date, SUM(po.Quantity) AS Total_quantity, SUM(p.Price_per_unit * po.Quantity) AS Total_cost
FROM Products AS p
INNER JOIN Purchase_orders AS po
ON p.Product_id = po.Product_id
WHERE po.Order_date BETWEEN '2025-05-01' AND '2025-05-31'
GROUP BY p.Product_name, po.Order_date
ORDER BY Total_cost DESC;

-- Display each suppliers name and email showing their most recent order date
SELECT s.Supplier_name, LOWER(s.Email) AS Email, DATE_FORMAT(MAX(po.Order_date), '%W, %d %m, %Y') AS Latest_order_date
FROM Suppliers AS s
LEFT JOIN Purchase_orders AS po ON s.Supplier_id = po.Supplier_id
GROUP BY s.Supplier_id, s.Supplier_name, s.Email
ORDER BY Latest_order_date DESC;

-- Show which countries supplied the least products this quarter
SELECT s.Supplier_id, s.Supplier_name, s.Supplier_country AS Country, SUM(po.Quantity) AS Total_supplied
FROM Purchase_orders AS po
INNER JOIN Suppliers AS s 
ON po.Supplier_id = s.Supplier_id
GROUP BY s.Supplier_id, s.Supplier_name, s.Supplier_country
ORDER BY Total_supplied ASC
LIMIT 3;

-- Due to a lack of demand this quarter, partnership with the company who supplied the least products has been cut and deleted from the database
SET @least_supplied:=(
SELECT s.Supplier_id 
FROM Purchase_orders po
JOIN Suppliers s ON po.Supplier_id = s.Supplier_id
WHERE po.Order_date BETWEEN '2025-04-01' AND '2025-06-30'
GROUP BY s.Supplier_id
ORDER BY SUM(po.Quantity) ASC
LIMIT 1);

DELETE FROM Suppliers
WHERE Supplier_id = @least_supplied;

-- Checking that the supplier has been removed from all related tables
SELECT * 
FROM Suppliers;

SELECT * 
FROM Purchase_orders;

SELECT *
FROM Products;
