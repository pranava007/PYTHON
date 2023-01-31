def biodate(**date):
    print(date)
biodate(name="ram",age=25,student="student",degree="MCA")

#defulte parameter
def location(name,city="salam"):
    print(name,city)
location(name="muthu")

#passing a list as an argument
def total(mark):
    return sum(mark)
print(total([22,33,44]))


def factorial(x):
    pass

factorial(5)

#recursive function
def factorial_1(x):
    if x==1:
        return 1
    else:
       return ( x*factorial_1(x-1) )

m=factorial_1(5)
print(m)

#lambda function
c = lambda a:a+50
print(c(30))

c = lambda a,b : a*b
print(c(33,44))