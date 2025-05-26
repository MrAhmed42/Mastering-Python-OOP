# Custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older."):
        self.message = message
        super().__init__(self.message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        print("Age is valid.")

# Example usage
try:
    check_age(15)
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")

# Valid case
try:
    check_age(20)
except InvalidAgeError as e:
    print(f"Custom Exception Caught: {e}")


    