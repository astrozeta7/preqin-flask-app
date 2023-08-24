Project Name

Preqin Flask Web Application
Description

This is a Flask web application that provides user registration, login, and random array generation functionality. The application uses SQLAlchemy for database management, Flask-Bcrypt for password hashing, and Flask-Login for user authentication.
Table of Contents

- Installation
- Usage
- Endpoints
- Contributing
- License
- Contact
Installation

1. Clone the repository:
git

2. Navigate to the project directory:
app

3. Create a virtual environment:
venv

4. Activate the virtual environment:
- For Windows:
activate
- For macOS/Linux:
activate

5. Install the required dependencies:
txt

6. Set up the environment variables:
- Create a .env file in the project root directory.
- Add the following variables to the .env file:
your_database_uri

7. Initialize the database:
upgrade
Usage

1. Activate the virtual environment (if not already activated):
- For Windows:
activate
- For macOS/Linux:
activate

2. Start the application:
run

3. Open your web browser and navigate to http://localhost:5000 to access the application.
Endpoints

- / - Home page that displays the index.html template.
- /register - User registration page. Allows users to create an account.
- /login - User login page. Allows registered users to log in.
- /logout - Logout endpoint. Logs out the currently logged-in user.
- /random_array - POST endpoint that generates a random array based on the provided sentence in the request JSON payload.
- /random_array_2 - POST endpoint that generates a random array based on the provided sentence in the request JSON payload.
Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

Please ensure that your contributions adhere to the coding standards and follow the project's guidelines.
License

This project is licensed under the MIT License.
Contact

For any questions or inquiries, please contact your-name.