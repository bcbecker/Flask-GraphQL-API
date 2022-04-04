from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from ..models import Department as DepartmentModel


'''
Types for DepartmentModel, based on mongoengine objects. Used for queries/mutations
'''


class DepartmentType(MongoengineObjectType):
    '''
    Department document
    '''
    class Meta:
        model = DepartmentModel
        interfaces = (Node,)
