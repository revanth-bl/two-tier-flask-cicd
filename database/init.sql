CREATE DATABASE IF NOT EXISTS devops;

USE devops;

CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO messages (name, message)
VALUES
('Admin', 'Welcome to the Two-Tier Flask CI/CD Project!');