CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('field_officer', 'admin') NOT NULL,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_status ENUM('active', 'inactive') DEFAULT 'active'
);


CREATE TABLE field_officers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    sir_name VARCHAR(50) NOT NULL,
    other_names VARCHAR(100),
    ps_number VARCHAR(50) NOT NULL UNIQUE,
    id_number VARCHAR(20) NOT NULL UNIQUE,
    phone_number VARCHAR(20) NOT NULL UNIQUE,
    work_station VARCHAR(100) NOT NULL,
    field_number VARCHAR(50),
    password_hash VARCHAR(255) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
