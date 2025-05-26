class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
# Create an instance
double = Multiplier(2)


# Check if the object is callable
print(callable(double)) # Output: True

result = double(20) # 20 * 2 = 40
print(result) # Output: 40