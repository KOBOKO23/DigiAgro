-- Create the 'users' table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(30) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    account_status ENUM('active', 'inactive') DEFAULT 'active'
);

-- Create the 'registration' table
CREATE TABLE registration (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,  -- Changed to registration_id to uniquely identify each record
    user_id INT,  -- Foreign key reference to the 'users' table
    first_name VARCHAR(10) NOT NULL,
    sir_name VARCHAR(10) NOT NULL,
    other_names VARCHAR(10),
    email VARCHAR(15) UNIQUE NOT NULL,
    ps_number VARCHAR(16) NOT NULL,
    id_number VARCHAR(15) NOT NULL,
    phone_number VARCHAR(10) NOT NULL,
    work_station VARCHAR(30) NOT NULL,
    password VARCHAR(20) NOT NULL,
    account_status ENUM('active', 'inactive') DEFAULT 'active',
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Define the foreign key constraint
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
