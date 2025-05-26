class Car:
    def __init__(self, brand):
        self.brand = brand # Public instance variable

    def start(self):
        print(f"The {self.brand} car has started.")

car1 = Car("BMW")

# Accessing public variable
print(f"Car Brand: {car1.brand}")

# Accessing public method
car1.start()