CREATE DATABASE ProductComparison;

USE ProductComparison;

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10,2),
    rating VARCHAR(50),
    rating_count VARCHAR(50),
    link TEXT,
    platform VARCHAR(50)  -- 'Amazon' or 'Flipkart'
);
SELECT * FROM products;