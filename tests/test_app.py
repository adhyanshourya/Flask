import unittest
from app import app
import json

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # Test that home page loads successfully
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        # Test adding a new todo item
        response = self.app.post('/add', data=dict(
            title='Test Todo',
            desc='Test Description'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Todo', response.data)

    def test_update_todo(self):
        # First add a todo
        self.app.post('/add', data=dict(
            title='Update Test',
            desc='Update Description'
        ))
        # Then test updating it
        response = self.app.get('/update/1')
        self.assertEqual(response.status_code, 200)

    def test_delete_todo(self):
        # First add a todo
        self.app.post('/add', data=dict(
            title='Delete Test',
            desc='Delete Description'
        ))
        # Then test deleting it
        response = self.app.get('/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Delete Test', response.data)

    def test_invalid_page(self):
        # Test accessing an invalid route
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()