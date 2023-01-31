class A:
    def display(self):
        print("The class is A")

class B(A):
    def display(self):
        print("The class is B")


class C(A):
    def display(self):
        print("The class is C")

class D(B,C):
    def display(self):
        print("The class is D")

obj=D()
obj.display()