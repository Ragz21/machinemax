import unittest
from server import app


class ServerTest(unittest.TestCase):

    def test_home_page(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/')
            self.assertEqual(response.status_code, 200)

    def test_home_page_data(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/')
            self.assertTrue(b'results' in response.data)

    def test_home_page_content(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/')
            self.assertEqual(response.content_type, 'application/json')

    def test_search_page(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/?query=qatar')
            self.assertEqual(response.status_code, 200)

    def test_search_page_data(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/?query=qatar')
            self.assertTrue(b'results' in response.data)

    def test_search_page_content(self):
        """
        GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid
        """

        # Create a test client using the Flask application configured for testing
        with app.test_client(self) as test_client:
            response = test_client.get('/?query=qatar')
            self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
