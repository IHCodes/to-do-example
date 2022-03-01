from flask_testing import TestCase
from application import app, db
from application.models import Todos
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            SECRET_KEY='secret',
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()

        task1 = Todos(task = "task")

        db.session.add(task1)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestCRUD(TestBase):

    def test_read_Todos(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Add New', str(response.data))
        self.assertIn('task', str(response.data))

    def test_delete_Todos(self):
        response = self.client.get(url_for('delete',id=1))
        self.assertNotIn('task', str(response.data))


