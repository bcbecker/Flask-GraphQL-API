import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from bson.objectid import ObjectId
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


class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(Employee)

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
    employee = graphene.Field(Employee)

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

        if _employee:
            _employee.save()

        return UpdateEmployee(employee=_employee)


class DeleteEmployee(graphene.Mutation):
    employee = graphene.Field(Employee)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(root, info, id):
        employee = EmployeeModel.objects.get(id=ObjectId(id))
        employee.delete()

        return DeleteEmployee(employee=employee)


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


schema = graphene.Schema(query=Query, mutation=Mutation, types=[
                         Department, Role, Task, Employee])
