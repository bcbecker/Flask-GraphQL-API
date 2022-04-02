import graphene
from bson.objectid import ObjectId
from ..models import Role as RoleModel
from .types import RoleType

'''
Mutations for the Role document
'''


class CreateRole(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        name = graphene.String(required=True)

    def mutate(root, info, name):

        _role = RoleModel(
            name=name
        )

        if _role:
            _role.save()

        return CreateRole(role=_role)


class UpdateRole(graphene.Mutation):
    role = graphene.Field(RoleType)

    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()

    def mutate(root, info, id, name=None):

        _role = RoleModel.objects.get(id=ObjectId(id))

        if name:
            _role.name = name

        if _role:
            _role.save()

        return UpdateRole(role=_role)


class DeleteRole(graphene.Mutation):
    _role = graphene.Field(RoleModel)

    class Arguments:
        id = graphene.ID(required=True)

    def mutate(root, info, id):
        _role = RoleModel.objects.get(id=ObjectId(id))
        _role.delete()

        return DeleteRole(role=_role)
