class father:
    def piecing(self):
        print("good piecing ")

class mother:
    def cook(self):
        print("cook ")
class son(father,mother):
    def grt(self):
        print("travel")

o=son()
o.piecing()
o.cook()
o.grt()
