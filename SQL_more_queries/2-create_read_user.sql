-- Script to create database hbtn_0d_2 and user_0d_2 with SELECT privilege only

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege only on the database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
