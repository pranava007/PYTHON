class student:
    def __init__(self,total):
        self._total=total

    def avarage(self):
        return  self._total/5

    def getter(self):
       return self._total

    def setter(self,t):
        self._total=t

    total = property( getter , setter )

o=student(400)
print(o.total)
print(o.avarage())
o.total=250
print(o.total)
print(o.avarage())



