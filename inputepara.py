para=[]
print("Enter tha para :")
while True:
    letter=input()
    if letter:
        para.append(letter)
    else:
        break
print(para.join())
