from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema


api = Blueprint('employees_api', __name__)


@api.route('/')
def hello_world():
    return 'Hello from GraphQL! Visit the /graphql route for the GraphiQl interface'


api.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema, graphiql=True
))
