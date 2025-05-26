class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
# Testing the static method without creating an instance
result = MathUtils.add(10, 42)
print(result)