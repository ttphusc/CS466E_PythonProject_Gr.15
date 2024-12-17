-- Tạo database nếu chưa có
CREATE DATABASE IF NOT EXISTS usermanagement;

-- Tạo user mới
CREATE USER 'phuc'@'localhost' IDENTIFIED BY 'phuc2003';

-- Cấp quyền cho user
GRANT ALL PRIVILEGES ON usermanagement.* TO 'phuc'@'localhost';
FLUSH PRIVILEGES;

SHOW DATABASES;
USE usermanagement;