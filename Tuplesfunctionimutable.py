a=(2,5.5,True,"muthu")#Tuble
print(type(a))
print(a[3])
b=list(a)
print(b)
print(type(b))
print(type(a))

for i in a:
    print(i)

if "muthu" in a:
    print("muthu found")
else:
    print("Not found")
print(len(a))
del a # detaleted function
a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=a+b
print(c)
print(c.count(5))
a=(1,2,3,4,5)
b=(1,2,3,4,5)
c=(a,b) #nested tuble
print(c)
print(c[0])
print(c[1])
print(c[0][2])

x = ("muthu",)*10
print(x)

a=(1,2,3,4,5)
print(min(a))
print(max(b))

a={1,2,3,4,5,6}
b={"a","b","c","d"}
c=a.union(b)
print(c)
a.update(b)
print(c)