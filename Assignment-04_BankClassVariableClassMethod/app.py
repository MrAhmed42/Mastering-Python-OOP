class Bank:
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

# Creating instances
customer1 = Bank("Ahmed")
customer2 = Bank("Ayesha")

# Displaying before change
print("Before bank name change:")
customer1.display()
customer2.display()

# Changing the bank name using class method
Bank.change_bank_name("Habib Bank")

# Displaying after change
print("\nAfter bank name change:")
customer1.display()
customer2.display()
