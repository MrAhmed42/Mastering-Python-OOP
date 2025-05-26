class Product:
    def __init__(self, price):
        self.__price = price # Private attribute

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number.")
        if value < 0:
            raise ValueError("Price cannot be negative!")
        self.__price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self.__price

product = Product(100)

print(product.price) # Access price via getter -> Output: 100

product.price = 150 # Update price using setter
print(product.price) # Output: 150

try:
    product.price = -50 # Try to set invalid negative price
except ValueError as e:
    print(e) # Output: Price cannot be negative!

try:
    product.price = "Ahmed" # Try to set invalid type price
except TypeError as e:
    print(e) # Output: Price must be a number.

del product.price  # Delete the price attribute, calls deleter