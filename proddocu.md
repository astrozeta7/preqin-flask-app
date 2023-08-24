# Random Array Generator API Documentation

Welcome to the documentation for the Random Array Generator API built with Flask. This documentation provides comprehensive information about the application's functionality, setup, usage, and more.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
- [Configuration](#configuration)
- [Database](#database)
- [User Management](#user-management)
- [Routes and Endpoints](#routes-and-endpoints)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [References](#references)

## Introduction

The Random Array Generator API is a Flask-based application that allows users to securely register, log in, and generate random arrays of floating-point numbers. The API is designed to provide a user-friendly and secure experience for accessing and utilizing random number generation.

## Prerequisites

Before using the Random Array Generator API, ensure you have the following prerequisites installed:

- Python 3.x
- Virtual environment (recommended)
- Database system (SQLite, MySQL, PostgreSQL, etc.)
- Environment variables (stored in a `.env` file)
- Basic knowledge of Flask and web APIs

## Installation and Setup

1. Clone the repository to your local machine.
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

- **Logging Configuration**: The application's logging is configured to log events with timestamp, name, log level, and message format.

## Database

The Random Array Generator API uses a database to store user information and manage authentication. By default, it uses the SQLAlchemy library to interact with the database.

- **Database Models**: The `User` model includes fields for `id`, `username`, and `password`.

## User Management

The application provides user registration, login, and logout functionalities. Users can securely register, log in, and access the API endpoints.

- **Registration**: Users can register with a unique username and a password following specific criteria.
- **Login**: Registered users can log in securely using their credentials.
- **Logout**: Logged-in users can log out of their sessions.

## Routes and Endpoints

- `/`: The root URL requires user authentication and displays the main interface.
- `/register`: Supports both GET and POST methods for user registration.
- `/login`: Supports both GET and POST methods for user login.
- `/logout`: Requires authentication and logs out the user.
- `/random_array`: Generates a random array based on the input sentence.
- `/random_array_2`: Generates another random array based on the input sentence.

## Running the Application

To run the application:

1. Ensure the database connection is configured in the `.env` file.
2. Run the following command to create database tables:
   ```bash
   python app.py
   ```
3. The application will start in development mode and can be accessed at `http://localhost:8000`.

## Testing

To run tests using the unittest framework:

```bash
python -m unittest discover tests
```

## Troubleshooting

Refer to the [Troubleshooting](#troubleshooting) section in the documentation for common issues and solutions.

## Contributing

- Contributions are welcome. Fork the repository, create a feature branch, make your changes, and submit a pull request.
- Please adhere to the project's code style and guidelines.

## References

- Flask: https://flask.palletsprojects.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Flask-Bcrypt: https://flask-bcrypt.readthedocs.io/
- Flask-Login: https://flask-login.readthedocs.io/
- Python Random Module: https://docs.python.org/3/library/random.html

---

By following this documentation, you can successfully set up, configure, and use the Random Array Generator API built with Flask. If you encounter any issues or have questions, please refer to the [Troubleshooting](#troubleshooting) section or reach out to the project maintainers. Happy coding!