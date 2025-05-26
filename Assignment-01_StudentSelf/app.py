# Define the Student class
class Student:
    def __init__(self, name, marks):
        # Initialize instance variables using 'self'
        self.name = name
        self.marks = marks

    def display(self):
        # Print student details
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Create student objects
student1 = Student("Ahmed", 92)
student2 = Student("Ali", 83)

# Call the display method
student1.display()
print()
student2.display()
