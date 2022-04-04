from ..models import Task as TaskModel
from graphene.relay import Node
from graphene_mongo import MongoengineObjectType
from ..models import Employee as EmployeeModel, Task as TaskModel


'''
Types for EmployeeModel and TaskModel, based on mongoengine objects. Used for queries/mutations
'''


class EmployeeType(MongoengineObjectType):
    '''
    Employee document
    '''
    class Meta:
        model = EmployeeModel
        interfaces = (Node,)


class TaskType(MongoengineObjectType):
    '''
    Task embedded document within Employee
    '''
    class Meta:
        model = TaskModel
        interfaces = (Node,)
