class granfather:
    def ownhoues(self):
        print("own house")
class father(granfather):
    def bike(self):
        print("own bike")
class son(father):
    def book(self):
        print("own book")
o=son()
o.ownhoues()
o.bike()
o.book()