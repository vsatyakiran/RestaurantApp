CREATE DATABASE zomato_db;
USE zomato_db;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON test_db.* TO 'username'@'localhost';
FLUSH PRIVILEGES;

CREATE TABLE IF NOT EXISTS restaurant (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    country_code INT,
    city VARCHAR(255),
    address VARCHAR(255),
    locality VARCHAR(255),
    locality_verbose VARCHAR(255),
    longitude FLOAT,
    latitude FLOAT,
    cuisines VARCHAR(255),
    average_cost_for_two FLOAT,
    currency VARCHAR(50),
    has_table_booking VARCHAR(3),
    has_online_delivery VARCHAR(3),
    is_delivering_now VARCHAR(3),
    switch_to_order_menu VARCHAR(3),
    price_range INT,
    aggregate_rating FLOAT,
    rating_color VARCHAR(20),
    rating_text VARCHAR(50),
    votes INT
);
