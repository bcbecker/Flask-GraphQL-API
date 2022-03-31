from api.models import (
    Department as DepartmentModel,
    Employee as EmployeeModel,
    Role as RoleModel,
    Task as TaskModel
)


def populate_db():

    engineering = DepartmentModel(name="Engineering")
    engineering.save()

    hr = DepartmentModel(name="Human Resources")
    hr.save()

    manager = RoleModel(name="manager")
    manager.save()

    engineer = RoleModel(name="engineer")
    engineer.save()

    debug = TaskModel(name="Debug")
    test = TaskModel(name="Test")

    tracy = EmployeeModel(name="Tracy", department=hr, roles=[
        engineer, manager], tasks=[])
    tracy.save()

    peter = EmployeeModel(
        name="Peter",
        department=engineering,
        manager=tracy,
        roles=[engineer],
        tasks=[debug, test],
    )
    peter.save()

    roy = EmployeeModel(
        name="Roy",
        department=engineering,
        manager=tracy,
        roles=[engineer],
        tasks=[debug],
    )
    roy.save()
