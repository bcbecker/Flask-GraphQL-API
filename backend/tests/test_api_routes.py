import unittest
from flask import current_app
from graphene.test import Client
from api import create_app, db
from api.models import Department, Role, Task, Employee
from api.schema import schema
from config import TestingConfig
from populate_db import populate_db


class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        '''
        Sets up the app environment for testing: creates flask_client, graphql_client,
        app context, and populates the db.
        '''
        self.app = create_app(TestingConfig)
        self.appctx = self.app.app_context()
        self.appctx.push()
        self.flask_client = self.app.test_client()
        self.graphql_client = Client(schema)
        populate_db()

    def tearDown(self):
        '''
        Tears down the set up flask_client, graphql_client, db, and app context.
        '''
        db.drop_database(TestingConfig.MONGODB_SETTINGS['db'])
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.flask_client = None
        self.graphql_client = None

    def test_app(self):
        '''
       Verify that the current app is the app set up in the setUp method.
        '''
        assert self.app is not None
        assert current_app == self.app
        assert db.collections() is not None
        assert self.graphql_client is not None
