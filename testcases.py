# unittest is a framework that provides a set of tools for organizing and running automated tests. 
# It helps you structure your tests, manage their execution, and perform assertions to check the expected behavior of your code. 
import unittest
import logging
import os
from app import app, db, User
from flask_testing import TestCase

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_TEST_DATABASE_URI') # Use an in-memory SQLite database
        return app

    def setUp(self):
        logger.info("Setting up test database...")
        db.create_all()

    def tearDown(self):
        logger.info("Tearing down test database...")
        db.session.remove()
        db.drop_all()

    def test_register(self):
        logger.info("Testing user registration...")
        response = self.client.post('/register', data={'username': 'testuser', 'password': 'TestTest123!'})
        self.assertEqual(response.status_code, 302)  # Expect a redirect after successful registration

    def test_login(self):
        logger.info("Testing user login...")
        user = User(username='testuser', password='TestTest123!')
        db.session.add(user)
        db.session.commit()
        response = self.client.post('/login', data={'username': 'testuser', 'password': 'TestTest123!'})
        self.assertEqual(response.status_code, 200)  # Expect a successful response after login

    def test_logout(self):
        logger.info("Testing user logout...")
        response = self.client.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)  # Expect a successful response after logout

    def test_random_array(self):
        logger.info("Testing random array generation...")
        response = self.client.post('/random_array', json={'sentence': 'test sentence'})
        data = response.get_json()        
        # Ensure the response contains the 'array' key
        self.assertTrue('array' in data)
        random_array = data['array']
        # Check if each item in the array is a float
        self.assertTrue(all(isinstance(item, float) for item in random_array))
        # Check if each number in the array is between 0 and 2
        self.assertTrue(all(0 <= item <= 2 for item in random_array))
        # Check if the length of the array is 500
        self.assertEqual(len(random_array), 500)

    def test_index_page(self):
        logger.info("Testing index page redirection...")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)  # Expect a redirect to the login page
        logger.info("Actual Redirect Location: %s", response.location)
        self.assertTrue('/login' in response.location)

if __name__ == '__main__':
    unittest.main()
