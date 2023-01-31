a=int(input("Mark 1 :"))
b=int(input("Mark 2 :"))
c=int(input("Mark 3 :"))
tum=a+b+c
print("Total marks",tum)
print("Average :",tum/3)
if a>=35 and b>=35 and c>=35:
    print("result :pass")
    if tum>=90 and tum<=100:
        print("A grade ")
    elif tum>=80 and tum<=89:
        print("B grade")
    elif tum>=70 and tum<=79:
        print("c grade")
    else:
        print("D grade")

else:
    print("result : faile")






