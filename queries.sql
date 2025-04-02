CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('field_officer', 'admin') NOT NULL,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_status ENUM('active', 'inactive') DEFAULT 'active'
);
