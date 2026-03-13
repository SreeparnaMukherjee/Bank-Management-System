CREATE DATABASE bank_system;

USE bank_system;

CREATE TABLE accounts (
    accnum BIGINT PRIMARY KEY,
    password VARCHAR(50),
    name VARCHAR(100),
    phone VARCHAR(20),
    email VARCHAR(100),
    address TEXT,
    current_balance FLOAT DEFAULT 0,
    savings_balance FLOAT DEFAULT 0,
    loan FLOAT DEFAULT 0
);