from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from ..models import Role as RoleModel


'''
Types for RoleModel, based on mongoengine objects. Used for queries/mutations
'''


class RoleType(MongoengineObjectType):
    '''
    Role document
    '''
    class Meta:
        model = RoleModel
        interfaces = (Node,)
