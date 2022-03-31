from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema


employees = Blueprint('employees', __name__)


@employees.route('/')
def hello_world():
    return 'Hello From Graphql'


employees.add_url_rule('/graphql', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema, graphiql=True
))
