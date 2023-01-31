name={"mass","yamuna","pranavamuthu","cool"}
print(name)
print(type(name))

print("------------------------------------------------------------------")

for i in name:
    print(i)

print("------------------------------------------------------------------")


name.add("sara") #one elament .add function use pannanum
print(name)
print("------------------------------------------------------------------")

a={"oviya","ruthura","yamuna","kkkkkk","ihdhwrehwoho"}
name.update(a) #more then elament  add panna update use pannanum
print(name)
print("------------------------------------------------------------------")

name.remove("oviya") #elament remove pannum ella  na error varum
print(name)
print("------------------------------------------------------------------")


name.discard("sara") #element remove pannum
print(name)

print("------------------------------------------------------------------")

a ={"hi","hello","welcome"}
b ={"thala","mass","use",}
c=a.union(b)#union  a and b value va sathu c la storge pannum ''''new elament la
print(c)

print("------------------------------------------------------------------")

d ={"hi","hello","welcome"}
c ={"thala","mass","use",}
d.update(c)#update a and b value sathu a stroge pannum
print(d)
print("------------------------------------------------------------------")



a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.symmetric_difference(b)#symmetric_difference a and b oda value comman na ella tha number ra print pannum
print(c)
a.symmetric_difference_update(b)#same but new value la storge panna ma a storge pannum
print(a)
c=a.intersection(b) #intersection a and b set la erucka comman value va print pannum
a.intersection_update(b)#intersecion_update a la stroge akum
print(a)
print(c)

print("------------------------------------------------------------------")




a={5,6,7}
b={5,6,7,8,9}
c = a.issubset(b) #a oda value totall la  b ulla la erucka erutha true
print(c)
c = a.issuperset(b) #b oda value totall la a ulla erucka
print(c)

c=a.isdisjoint(b)# a and b la oru value kuda commana ella na true
print(c)
