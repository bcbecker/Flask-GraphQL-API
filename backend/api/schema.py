import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField
from .models import (
    Department as DepartmentModel,
    Role as RoleModel,
    Employee as EmployeeModel
)
from .department.types import DepartmentType
from .role.types import RoleType
from .employee.types import EmployeeType, TaskType

from .department.mutations import CreateDepartment, UpdateDepartment, DeleteDepartment
from .role.mutations import CreateRole, UpdateRole, DeleteRole
from .employee.mutations import CreateEmployee, UpdateEmployee, DeleteEmployee

'''
Schema, including the Query and Mutation object types
'''


class Query(graphene.ObjectType):
    node = Node.Field()
    department = graphene.Field(DepartmentType, name=graphene.String())
    role = graphene.Field(RoleType, name=graphene.String())
    employee = graphene.Field(EmployeeType, name=graphene.String())

    all_departments = MongoengineConnectionField(DepartmentType)
    all_roles = MongoengineConnectionField(RoleType)
    all_employees = MongoengineConnectionField(EmployeeType)

    def resolve_department(root, info, name):
        return DepartmentModel.objects.get(name=name)

    def resolve_role(root, info, name):
        return RoleModel.objects.get(name=name)

    def resolve_employee(root, info, name):
        return EmployeeModel.objects.get(name=name)


class Mutation(graphene.ObjectType):
    create_department = CreateDepartment.Field()
    update_department = UpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()

    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()

    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, types=[
                         DepartmentType, RoleType, TaskType, EmployeeType])
