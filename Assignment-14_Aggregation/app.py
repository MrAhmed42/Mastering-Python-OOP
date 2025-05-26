class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee Name: {self.name}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee # Aggregation: Department HAS-A reference to Employee

    def show_details(self):
        print(f"Department: {self.dept_name}")
        self.employee.display() # Access Employee's method

emp = Employee("Ahmed")

# Pass it to Department – Aggregation relationship
department = Department("IT", emp)

department.show_details()   

