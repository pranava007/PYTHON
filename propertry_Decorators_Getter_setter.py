class student:
    def __init__(self,total):
        self._total=total

    def avarage(self):
        return  self._total/5
    @property
    def total(self):
       return self._total
    @total.setter
    def total(self,t):
        self._total=t
o=student(400)
print(o.total)
print(o.avarage())
o.total=250
print(o.total)
print(o.avarage())



