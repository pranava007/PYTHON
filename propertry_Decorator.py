class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age
       # self.msg=self.name+ "  age is " +str(self.age)
    @property
    def msg(self):
        return self.name + "  age is " + str(self.age)

o=user("pranavamuthu",21)

print(o.name)
print(o.age)
o.age=22
print(o.msg)


