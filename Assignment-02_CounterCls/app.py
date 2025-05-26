class Counter:
    # Class variable to track the number of objects
    count = 0

    def __init__(self):
        # Each time an object is created, increment the count
        Counter.count += 1

    @classmethod
    def display_count(cls):
        # Class method to display the count using 'cls'
        print(f"Total objects created: {cls.count}")


# Creating objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the total number of objects created
Counter.display_count()
