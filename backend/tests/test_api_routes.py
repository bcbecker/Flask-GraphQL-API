from snapshottest import TestCase
from flask import current_app
from graphene.test import Client
from config import TestingConfig
from populate_db import populate_db
from api import create_app, db
from api.schema import schema


class TestFlaskApp(TestCase):

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
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.flask_client = None
        self.graphql_client = None
        self._drop_db_collections()

    def _drop_db_collections(self):
        '''
        Helper function to drop all collections from the test db.
        '''
        collections_list = db.get_db().list_collection_names()

        for collection_name in collections_list:
            db.get_db().drop_collection(collection_name)

    def test_app(self):
        '''
        Verify that the current app is the app set up in the setUp method.
        '''
        assert self.app is not None
        assert current_app == self.app
        assert db.get_db().list_collection_names() is not None
        assert self.graphql_client is not None

    def test_api_home(self):
        '''
        Given a test client, send a GET request to the '/' route.
        Verify status codes and content.
        '''
        response_200 = self.flask_client.get('/',
                                             headers={
                                                 'Content-Type': 'application/json'},
                                             follow_redirects=True
                                             )
        assert response_200.status_code == 200
        assert response_200.request.path == '/'
        assert response_200.data == b'Hello from GraphQL! Visit the /graphql route for the GraphiQl interface'

    def test_api_graphql_all_employees(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for all employees in the Employee collection. Assert the correct data is
        returned.
        '''
        from .test_queries.all_employees import all_employees_query

        self.assertMatchSnapshot(
            self.graphql_client.execute(all_employees_query))

    def test_api_graphql_all_departments(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for all departments in the Department collection. Assert the correct data is
        returned.
        '''
        from .test_queries.all_departments import all_departments_query

        self.assertMatchSnapshot(
            self.graphql_client.execute(all_departments_query))

    def test_api_graphql_all_roles(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for all roles in the Role collection. Assert the correct data is
        returned.
        '''
        from .test_queries.all_roles import all_roles_query

        self.assertMatchSnapshot(self.graphql_client.execute(all_roles_query))

    def test_api_graphql_employee(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for an employee in the Employee collection by the 'name' parameter. Assert
        the correct data is returned.
        '''
        from .test_queries.employee import employee_query

        self.assertMatchSnapshot(self.graphql_client.execute(employee_query))

    def test_api_graphql_department(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for a department in the Department collection by the 'name' parameter. Assert
        the correct data is returned.
        '''
        from .test_queries.department import department_query

        self.assertMatchSnapshot(self.graphql_client.execute(department_query))

    def test_api_graphql_role(self):
        '''
        Given a test client, send a GET request to the '/graphql' route with a query
        for a role in the Role collection by the 'name' parameter. Assert the correct
        data is returned.
        '''
        from .test_queries.role import role_query

        self.assertMatchSnapshot(self.graphql_client.execute(role_query))
