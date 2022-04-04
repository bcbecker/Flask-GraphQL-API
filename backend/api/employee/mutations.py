import graphene
from bson.objectid import ObjectId
from ..models import (
    Department as DepartmentModel,
    Employee as EmployeeModel,
    Role as RoleModel,
    Task as TaskModel
)
from .types import EmployeeType

'''
Mutations for the Employee document
'''


class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)

    class Arguments:
        name = graphene.String(required=True)
        department_id = graphene.ID(required=True)
        roles_id = graphene.List(graphene.ID, required=True)
        manager_id = graphene.ID()
        tasks = graphene.List(graphene.String)

    def mutate(root, info, name, department_id, roles_id, manager_id=None, tasks=None):

        _department = DepartmentModel.objects.get(id=ObjectId(department_id))
        _roles = [RoleModel.objects.get(id=ObjectId(_role_id))
                  for _role_id in roles_id]
        _manager = EmployeeModel.objects.get(id=ObjectId(manager_id))

        if tasks:
            tasks = [TaskModel(name=_name) for _name in tasks]

        _employee = EmployeeModel(
            name=name,
            department=_department,
            manager=_manager,
            roles=_roles,
            tasks=tasks,
        )

        if _employee:
            _employee.save()

        return CreateEmployee(employee=_employee)


class UpdateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        department_id = graphene.ID()
        roles_id = graphene.List(graphene.ID)
        manager_id = graphene.ID()
        tasks = graphene.List(graphene.String)

    def mutate(root, info, id, name=None, department_id=None, roles_id=None, manager_id=None, tasks=None):

        _employee = EmployeeModel.objects.get(id=ObjectId(id))

        if name:
            _employee.name = name

        if department_id:
            _department = DepartmentModel.objects.get(
                id=ObjectId(department_id))
            _employee.department = _department

        if roles_id:
            _roles = [RoleModel.objects.get(
                id=ObjectId(_role_id)) for _role_id in roles_id]
            _employee.roles = _roles

        if manager_id:
            _manager = EmployeeModel.objects.get(
                id=ObjectId(manager_id))
            _employee.manager = _manager

        if tasks:
            _tasks = [TaskModel(name=_name) for _name in tasks]
            _employee.tasks = _tasks

        _employee.save()

        return UpdateEmployee(employee=_employee)


class DeleteEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(root, info, id):
        _employee = EmployeeModel.objects.get(id=ObjectId(id))
        _employee.delete()

        return DeleteEmployee(employee=_employee)
