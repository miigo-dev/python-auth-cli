# PyAuth-CLI
A simple CLI-based user registration and authentication system using SQLite and Bcrypt written in Python.

A simple command-line interface for user registration and login using SQLite database and bcrypt library for password hashing and verification. The code creates a 'users' table in a SQLite database, where new user information is stored after passing the validation checks. The validation checks include username and password criteria, such as:
  - only allowing alphanumeric characters in the username
  - requiring the password to be at least 8 characters long with at least one uppercase letter and one number

The code also includes a login function that checks the entered username and password against the stored hashed password using bcrypt's `checkpw()` function.
