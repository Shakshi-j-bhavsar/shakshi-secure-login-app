# Shakshi Secure Login Application (PostgreSQL)

A beginner-friendly "secure login web application" built using **Flask (Python)** and **PostgreSQL**, focusing on **authentication, authorization, and security best practices** rather than UI design.

This project was created as a learning exercise to understand how secure backend logic works in real-world web applications.



##  Project Description

This application implements a **secure user authentication system** with proper password handling, session management, and role-based access control.  

The main goal of the project is to learn and apply:
- Secure login & signup workflows
- Password hashing
- Database integration using PostgreSQL
- Secure session handling
- Input validation and access control


## Features

- User signup and login
- Secure password hashing (bcrypt)
- PostgreSQL database integration
- Session-based authentication
- Role-based authorization (user / admin)
- Protected routes (dashboard, admin panel)
- Secure session handling using Flask sessions
- Environment variable configuration using `.env`



## Project Folder Structure

shakshi-secure-login-app.pgsql/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── .env # Environment variables (not pushed to GitHub)
├── .gitignore # Files to ignore in version control
│
├── templates/ # HTML templates
│ ├── login.html
│ ├── signup.html
│ ├── dashboard.html
│ └── admin.html
│
└── static/ # Static files (CSS, JS if added later)


## Technologies Used

- Python 3
- Flask
- PostgreSQL
- psycopg2
- bcrypt
- python-dotenv
- HTML (basic templates)

---##----

##Setup & Installation
=> Clone the Repository
git clone <repository-url>
cd shakshi-secure-login-app.pgsql


# Create a Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt

# Create PostgreSQL Database
Login to PostgreSQL:
psql -U postgres

Create database:
CREATE DATABASE shakshi_secure_login_app;

# Create Required Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

# Configure Environment Variables
Create a .env file:

DB_HOST=localhost
DB_PORT=5432
DB_NAME=my_secure_login_app
DB_USER=postgres
DB_PASSWORD=My_Password
SECRET_KEY=my_generated_secret_key


# Run the Application
python app.py

# Security Practices Implemented
Passwords are never stored in plain text
Password hashing using bcrypt
Session protection using Flask SECRET_KEY
Role-based access control
Environment variables for sensitive data
SQL injection prevention using parameterized queries

# Usage
Register a new user using the signup page
Login using valid credentials
Access dashboard after login
Admin users can access admin panel
Unauthorized users are restricted from protected routes

# Important Disclaimer
This project is intended for educational and learning purposes only.
It demonstrates basic security practices but is not production-ready.

# Author
Shakshi
Secure Web Application – Internship Project
Focused on backend security & authentication fundamentals

