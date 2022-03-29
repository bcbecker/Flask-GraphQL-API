from flask import Blueprint
from flask_graphql import GraphQLView
from .schema import schema_query


employees = Blueprint('employees', __name__)


@employees.route('/')
def hello_world():
    return 'Hello From Graphql'


employees.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
    'graphql-query',
    schema=schema_query, graphiql=True
))
