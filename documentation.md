step 0 : prequirements
            1. python3
            3. pip3
            4. 
Step 1 : First unzip productionrelease1.1.zip
Step 2 : Let's understand folder structure
            preductionrelease1.1
                preqin
                    - instance
                        - srn.db
                    - static
                        - styles.css
                    - templates
                        - index.html
                        - login.html
                        - register.html
                    - .env
                    - app.py
                    - create_db.py
                    - Dockerfile
                    - readme.md
                    - requirements.txt
                    - testcases.py
                    - wsgi.py
step 3 : Create a virtual environment




To run the code in development and with debugger on pleae execute below cmd


Flask is the core class for creating a Flask application and handling HTTP requests.
render_template is used to render HTML templates in your views.
request handles incoming HTTP requests and allows you to access data from the request.
redirect and url_for are used for URL redirection.
jsonify creates JSON responses.
flash is used for displaying flash messages to users.
get_flashed_messages retrieves flashed messages.
SQLAlchemy is an Object-Relational Mapping (ORM) library for database management.
Bcrypt provides functions for hashing passwords securely.
LoginManager is used for managing user authentication.
UserMixin is a mixin class for implementing user-related functionalities.
login_user, login_required, logout_user, and current_user are used for user authentication and session management.
random is used to generate random values.
logging is used for logging application events.
sys provides access to Python interpreter variables and functions.
load_dotenv loads environment variables from a .env file.
datetime is used for working with dates and times.
os provides functions for interacting with the operating system.
re is used for working with regular expressions.




logging.basicConfig(): This call configures the logging system. It sets the logging level to INFO, which means only messages with a severity level of INFO or higher will be logged.

handlers=[logging.StreamHandler(sys.stdout)]: This sets up a handler to direct log messages to the console (stdout). The StreamHandler sends log records to a stream (file-like object), and in this case, we're using sys.stdout to send messages to the standard output (console).

format='%(asctime)s - %(name)s - %(levelname)s - %(message)s': This sets the format of the log messages. The placeholders (%(asctime)s, %(name)s, %(levelname)s, %(message)s) are replaced with the actual values when a log message is generated. For example, %(asctime)s is replaced with the timestamp of the log record.

datefmt='%Y-%m-%d %H:%M:%S': This specifies the format for the timestamp in the log messages. %Y represents the year, %m represents the month, %d represents the day, %H represents the hour, %M represents the minute, and %S represents the second.

logging.getLogger(__name__): This creates a logger instance specific to the current module or script. The __name__ variable contains the name of the current module or script. Using this logger, you can add log messages to your code with different severity levels, and they will be processed according to the configuration you set up earlier.

load_dotenv(): This function is used to load environment variables from a .env file located in the same directory as your script. Environment variables are typically used to store sensitive or configuration-specific information outside your code. By using a .env file, you can keep these variables separate from your code and version control.

app = Flask(__name__, static_folder='static'): This line creates a Flask application instance named app. The __name__ parameter specifies the name of the current module. The static_folder parameter specifies the folder from which static files like CSS, JavaScript, and images will be served.

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY'): This line sets the SECRET_KEY configuration option for the Flask app. The SECRET_KEY is used for cryptographic operations like generating secure tokens or cookies. It's important to keep this key secret and not hardcode it in your code.

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI'): This line sets the SQLALCHEMY_DATABASE_URI configuration option for the Flask app. It specifies the connection URL for the SQLAlchemy database. This should be a URL in the format of database://user:password@host:port/database_name.

db = SQLAlchemy(app): This line creates a SQLAlchemy database instance db using the Flask app. This instance will be used to interact with the database.

bcrypt = Bcrypt(app): This line creates a Bcrypt instance bcrypt using the Flask app. Bcrypt is a library used for hashing passwords securely. This instance will be used to hash and verify passwords.

Remember that values for SECRET_KEY and SQLALCHEMY_DATABASE_URI should be stored in a secure way, such as environment variables or a separate configuration file, to keep sensitive information out of your source code. The usage of environment variables (os.getenv) assumes that you have defined these environment variables using a .env file or through your server's environment.





