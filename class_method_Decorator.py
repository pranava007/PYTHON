class student:
    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        student.count += 1

    def printdetile(slfe):
      print( slfe.name,"age is a",slfe.age)

    @classmethod
    def total(cls):
        return cls.count

o = student("muthu",21)
o = student("muthu",21)
o = student("muthu",21)
o.printdetile()
o.printdetile()
o.printdetile()
print(o.total())


