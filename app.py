# Import the Flask class for creating the Flask application
from flask import Flask, render_template, request, redirect, url_for, jsonify, flash, get_flashed_messages
# Import SQLAlchemy for database management
from flask_sqlalchemy import SQLAlchemy
# Import Bcrypt for password hashing
from flask_bcrypt import Bcrypt
# Import LoginManager and UserMixin for user authentication and management
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
# Import the random module for generating random values
import random 
# Import the logging module for logging application events
import logging
# Import the sys module for interacting with the Python interpreter
import sys
# Import the load_dotenv function for loading environment variables from a .env file
from dotenv import load_dotenv
# Import the datetime module for working with date and time
import datetime
# Import the os module for interacting with the operating system
import os
# Import the re module for regular expressions (string pattern matching)
import re 


# Configure logging settings
logging.basicConfig(
    level=logging.INFO,                         # Set the logging level to INFO
    handlers=[logging.StreamHandler(sys.stdout)],  # Configure a handler to log messages to stdout (console)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Define the format of the log messages
    datefmt='%Y-%m-%d %H:%M:%S'                  # Define the date and time format for log messages
)
# Get a logger instance for the current module or script
logger = logging.getLogger(__name__)

# Create a Flask application instance with the name of the current module
# and specify the 'static' folder for serving static files
app = Flask(__name__, static_folder='static')
# Set the 'SECRET_KEY' configuration for the Flask app
# The secret key is used for cryptographic operations and should be kept secure
# Load environment variables from a .env file into the current environment
load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# Set the 'SQLALCHEMY_DATABASE_URI' configuration for the Flask app
# This URI specifies the database connection URL for SQLAlchemy to use
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# Create a SQLAlchemy database instance using the Flask app
db = SQLAlchemy(app)
# Define a User class that inherits from db.Model and UserMixin
# The UserMixin class provides additional methods and attributes required by Flask-Login to manage user authentication and sessions.
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
# Create a Bcrypt instance using the Flask app
# Bcrypt is used for hashing and checking passwords securely
bcrypt = Bcrypt(app)
# Create a LoginManager instance using the Flask app
# This line creates a LoginManager instance named login_manager using the Flask app. 
# The LoginManager is used to manage user authentication and sessions in a Flask application.
login_manager = LoginManager(app)
# Set the login view for LoginManager
# When a user tries to access a protected route without being authenticated, they will be redirected to the route specified in login_view, which in this case is 'login'. 
# This means that if a user tries to access a protected route and is not logged in, they will be redirected to the login page.
login_manager.login_view = 'login'

# Register a user loader function for the LoginManager
# This function is called to load a user from the database based on their user ID
@login_manager.user_loader
def load_user(user_id):
    logger.info('extracting user...')
    logger.info(f'extracting user {user_id}...')
    # Retrieve and return the user from the database based on the user ID
    return User.query.get(int(user_id))

# Define a route for the root URL ('/') of the Flask application
# The route handler requires authentication (if @login_required is enabled)
# @app.route('/'): This decorator defines a route handler for the root URL '/' of the Flask application. 
# When a user accesses the root URL, this function will be executed.
@app.route('/')
@login_required
def index():
    logger.info('processing index route...')
    return render_template('index.html')

# Define a route for user registration with support for both GET and POST methods
@app.route('/register', methods=['GET', 'POST'])
def register():
    logger.info("processing user registration...")
    if request.method == 'POST':
        try:
            username = request.form['username']
            # Check if a user with the same username already exists in the database
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                raise Exception('Username already exists. Please choose a different username.')           
            password = request.form['password']
            # Check password length
            if len(password) < 8:
                raise Exception('Password must be at least 8 characters long.')
            # Check for at least one uppercase letter
            if not re.search(r'[A-Z]', password):
                raise Exception('Password must contain at least one uppercase letter.')
            # Check for at least one lowercase letter
            if not re.search(r'[a-z]', password):
                raise Exception('Password must contain at least one lowercase letter.')
            # Check for at least one digit
            if not re.search(r'\d', password):
                raise Exception('Password must contain at least one digit.')
            # Check for at least one special character
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                raise Exception('Password must contain at least one special character.')
            # Generate a hashed password using Bcrypt
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password=hashed_password)
            # Add the new user to the database session and commit the transaction
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            error_message = 'Registration failed: ' + str(e)
            flash(error_message, 'error')
            logger.info(error_message)
            return render_template('register.html')
    return render_template('register.html')

# Define a route for user login with support for both GET and POST methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if the user is already authenticated (logged in)
    if current_user.is_authenticated:
        logger.info("authenticating user...")
        return redirect(url_for('index'))
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        try:
            user = User.query.filter_by(username=request.form['username']).first()
            if user and bcrypt.check_password_hash(user.password, request.form['password']):
                # Log the user in using the 'login_user' function
                login_user(user)
                return redirect(url_for('index'))
            else:
                raise Exception('Invalid username or password')
        except Exception as e:
            error_message = 'Login failed: ' + str(e)
            flash(error_message, 'error')
            logger.info(error_message)
            return render_template('login.html')
    # If the request method is GET, render the 'login.html' template
    return render_template('login.html')

# Define a route for user logout
# The route handler requires authentication (if @login_required is enabled)
@app.route('/logout')
@login_required
def logout():
    logger.info("logging out...")
    logout_user()
    return redirect(url_for('login'))

# Define a route for generating a random array based on input sentence
@app.route('/random_array', methods=['POST'])
def random_array():
    try:
        data = request.get_json()
        sentence = data.get('sentence', '')
        if not sentence:
            return jsonify(error='Input sentence missing'), 400
        else:
            # Seed the random number generator with the provided sentence
            random.seed(sentence)
        random_array = [random.uniform(0, 2) for _ in range(500)]
        logger.info("processing random array generator")
        return jsonify(array=random_array)
    except Exception as e:
        logger.info(e)
        return jsonify(error=str(e)), 500
# Define a route to test in postman
@app.route('/random_array_2', methods=['POST'])
def random_array_2():
    try:
        data = request.get_json()
        sentence = data.get('sentence', '')
        if not sentence:
            return jsonify(error='Input sentence missing'), 400
        else:
            random.seed(sentence)
        random_array = [random.uniform(0, 2) for _ in range(500)]
        logger.info("processing random array generator")
        return random_array
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    # Create all database tables within the app context
    with app.app_context():
        db.create_all()
    logger.info("started running the random array generator application in development mode")
    app.run(debug=True, host='0.0.0.0', port=8000)
    


