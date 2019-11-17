DROP DATABASE IF EXISTS supermarketdb;
CREATE DATABASE supermarketdb;
USE supermarketdb;
CREATE TABLE supermarket (
    name VARCHAR(255) NOT NULL,
    id BIGINT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);
CREATE TABLE employee (
    name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    id BIGINT NOT NULL AUTO_INCREMENT,
    works_at BIGINT,
    manager_id BIGINT,
    salary BIGINT,
    phone VARCHAR(255),
    PRIMARY KEY (id),
    FOREIGN KEY (works_at)
        REFERENCES supermarket (id)
);
CREATE TABLE manager (
    id BIGINT NOT NULL AUTO_INCREMENT,
    employee_id BIGINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (employee_id)
        REFERENCES employee (id)
);
CREATE TABLE department (
    name VARCHAR(255) NOT NULL,
    id BIGINT NOT NULL AUTO_INCREMENT,
    store_id BIGINT,
    PRIMARY KEY (id),
    FOREIGN KEY (store_id)
        REFERENCES supermarket (id)
);


SHOW COLUMNS FROM employee;
SHOW COLUMNS FROM manager;