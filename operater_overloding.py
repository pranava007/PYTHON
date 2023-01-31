"""
a=10
b=20
print(a+b)

a="pranavamuthu"
b="yamuna"
print(a+b)
"""
class add:
    def __init__(self,a):
        self.a=a

    def __add__(self, other):
        return o.a + o2.a

o=add(20)
o2=add(20)
print("total =",o.a + o2.a)



