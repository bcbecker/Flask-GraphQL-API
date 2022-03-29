import unittest
import uuid
from flask import current_app
from app import create_app, db
from app.models import User
from config import TestingConfig


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        '''
        Sets up the app environment for testing: creates db, test_client, and app context.
        '''
        self.app = create_app(TestingConfig)
        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        '''
        Tears down the set up test_client, db, and app context.
        '''
        db.drop_all()
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def _populate_db(self):
        '''
        Helper function to populate the db with a user for testing.
        '''
        #TODO: use faker with mocked mongoengine
        user = User(
                public_id=str(uuid.uuid4()),
                username='Admin',
                email='admin@gmail.com'
            )
        user.set_password('adminisabadpassword')
        user.save()
    
    def test_app(self):
        '''
       Verify that the current app is the app set up in the setUp method.
        '''
        assert self.app is not None
        assert current_app == self.app
