import unittest
from app import db, Todo

class ModelTestCase(unittest.TestCase):
    def setUp(self):
        # Set up test database
        db.create_all()

    def tearDown(self):
        # Clean up after each test
        db.session.remove()
        db.drop_all()

    def test_todo_creation(self):
        # Test Todo model
        todo = Todo(title='Test Todo', desc='Test Description')
        db.session.add(todo)
        db.session.commit()

        # Query the todo
        saved_todo = Todo.query.filter_by(title='Test Todo').first()
        self.assertIsNotNone(saved_todo)
        self.assertEqual(saved_todo.desc, 'Test Description')

    def test_todo_deletion(self):
        # Create and then delete a todo
        todo = Todo(title='Delete Test', desc='Delete Description')
        db.session.add(todo)
        db.session.commit()

        db.session.delete(todo)
        db.session.commit()

        # Verify deletion
        deleted_todo = Todo.query.filter_by(title='Delete Test').first()
        self.assertIsNone(deleted_todo)

if __name__ == '__main__':
    unittest.main()