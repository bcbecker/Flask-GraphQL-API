import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from .models import (
    Department as DepartmentModel,
    Employee as EmployeeModel,
    Role as RoleModel,
    Task as TaskModel
)

'''
TYPES
'''

class Department(MongoengineObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (Node,)


class Role(MongoengineObjectType):
    class Meta:
        model = RoleModel
        interfaces = (Node,)


class Task(MongoengineObjectType):
    class Meta:
        model = TaskModel
        interfaces = (Node,)


class Employee(MongoengineObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (Node,)


'''
MUTATIONS
'''
#TODO: write mutations for Employee 

class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(Employee)

    class Arguments:
        pass

class UpdateEmployee(graphene.Mutation):
    employee = graphene.Field(Employee)

    class Arguments:
        pass

class DeleteEmployee(graphene.Mutation):
    employee = graphene.Field(Employee)

    class Arguments:
        pass


'''
QUERIES
'''


class Query(graphene.ObjectType):
    node = Node.Field()
    department = graphene.Field(Department, name=graphene.String())
    role = graphene.Field(Role, name=graphene.String())
    employee = graphene.Field(Employee, name=graphene.String())

    all_departments = MongoengineConnectionField(Department)
    all_roles = MongoengineConnectionField(Role)
    all_employees = MongoengineConnectionField(Employee)

    def resolve_department(root, info, name):
        return DepartmentModel.objects.get(name=name)

    def resolve_role(root, info, name):
        return RoleModel.objects.get(name=name)

    def resolve_employee(root, info, name):
        return EmployeeModel.objects.get(name=name)


class Mutation(graphene.ObjectType):
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
    

'''
SCHEMA
'''


schema = graphene.Schema(query=Query, types=[Department, Role, Task, Employee])
