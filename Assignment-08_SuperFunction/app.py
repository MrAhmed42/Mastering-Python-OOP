class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called for: {self.name}, Subject: {self.subject}")

teacher = Teacher("Aslam", "Statistics")
