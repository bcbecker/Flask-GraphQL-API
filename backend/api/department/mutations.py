import graphene
from bson.objectid import ObjectId
from ..models import Department as DepartmentModel
from .types import DepartmentType

'''
Mutations for the Department document
'''


class CreateDepartment(graphene.Mutation):
    department = graphene.Field(DepartmentType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(root, info, name):

        _department = DepartmentModel(
            name=name
        )

        if _department:
            _department.save()

        return CreateDepartment(department=_department)


class UpdateDepartment(graphene.Mutation):
    department = graphene.Field(DepartmentType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    def mutate(root, info, id, name=None):

        _department = DepartmentModel.objects.get(id=ObjectId(id))

        if name:
            _department.name = name

        if _department:
            _department.save()

        return UpdateDepartment(department=_department)


class DeleteDepartment(graphene.Mutation):
    department = graphene.Field(DepartmentModel)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(root, info, id):
        _department = DepartmentModel.objects.get(id=ObjectId(id))
        _department.delete()

        return DeleteDepartment(department=_department)
