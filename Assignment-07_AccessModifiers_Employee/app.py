class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary # Protected variable (convention)
        self.__ssn = ssn   # Private variable 

# Creating an Employee object
employee = Employee("Ahmed", 1000000, "123-45-6789")

# Accessing public variable
print(f"Public - Name: {employee.name}")

# Accessing protected variable (possible, but not recommended directly)
print(f"Protected - Salary: {employee._salary}")

# Trying to access private variable directly (will cause AttributeError)
try:
    print(f"Private - SSN: {employee.__ssn}")
except AttributeError:
    print("Private - SSN: Cannot access directly (AttributeError)")



