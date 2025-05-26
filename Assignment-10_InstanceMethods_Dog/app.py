class Dog:
    def __init__(self, name, breed):
        self.name = name # Instance variable
        self.breed = breed # Instance variable

    def bark(self):
        print(f"{self.name} says: Woof! Woof!")

dog = Dog("Buddy", "Golden Retriever")
dog.bark()