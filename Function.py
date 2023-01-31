def name():
    print("HI~PRANAVA MUTHU")
name()

#No return type without argument function

def add():
    a=int(input("Enter value:"))
    b=int(input("Enter value:"))
    c=a+b
    print(c)
add()

#No return type with argument function

def sub(A,B):
    C=A-B
    print("Totall value :",C)
sub(22,33)

# Return type without argument function
def mul():
    a=int(input("enter the value :"))
    b=int(input("enter the value :"))
    c=a*b
    return c

print(mul())



#Return type with argument function
def mul(a,b):
    c=a*b
    return c
x=mul(2,3)
print(x)