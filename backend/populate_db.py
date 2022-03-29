from api.models import Department, Employee, Role, Task


def populate_db():
    
    engineering = Department(name="Engineering")
    engineering.save()

    hr = Department(name="Human Resources")
    hr.save()

    manager = Role(name="manager")
    manager.save()

    engineer = Role(name="engineer")
    engineer.save()

    debug = Task(name="Debug")
    test = Task(name="Test")

    tracy = Employee(name="Tracy", department=hr, roles=[engineer, manager], tasks=[])
    tracy.save()

    peter = Employee(
        name="Peter",
        department=engineering,
        leader=tracy,
        roles=[engineer],
        tasks=[debug, test],
    )
    peter.save()

    roy = Employee(
        name="Roy",
        department=engineering,
        leader=tracy,
        roles=[engineer],
        tasks=[debug],
    )
    roy.save()
