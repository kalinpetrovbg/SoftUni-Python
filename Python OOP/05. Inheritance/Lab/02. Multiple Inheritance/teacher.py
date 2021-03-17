from project.person import Person
from project.employee import Employee

class Teacher(Person, Employee):
    def __init__(self):
        pass

    @staticmethod
    def teach():
        return "teaching..."
