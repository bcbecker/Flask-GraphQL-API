from datetime import datetime
from api import db


class Department(db.Document):

    meta = {"collection": "department"}
    name = db.StringField()


class Role(db.Document):

    meta = {"collection": "role"}
    name = db.StringField()


class Task(db.EmbeddedDocument):

    name = db.StringField()
    deadline = db.DateTimeField(default=datetime.now)


class Employee(db.Document):

    meta = {"collection": "employee"}
    name = db.StringField()
    hired_on = db.DateTimeField(default=datetime.now)
    department = db.ReferenceField(Department)
    roles = db.ListField(db.ReferenceField(Role))
    leader = db.ReferenceField("Employee")
    tasks = db.ListField(db.EmbeddedDocumentField(Task))
