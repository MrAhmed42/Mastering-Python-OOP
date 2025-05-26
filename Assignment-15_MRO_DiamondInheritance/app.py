class A:
    def show(self):
        print("Show method from class A")

class B(A):
    def show(self):
        print("Show method from class B")


class C(A):
    def show(self):
        print("Show method from class C")

class D(B, C): # Diamond Inheritance
    pass 

d = D()
d.show()


# To observe MRO
print(D.__mro__)