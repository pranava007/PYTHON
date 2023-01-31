user={
    "name":"pranavamuthu",
    "Age":25,
    "marraide":False,
    "stutend":True
}
print(user)
print(type(user))
print(user["name"])
print(user["Age"])
print(user["marraide"])
print(user["stutend"])
print(user.get('Age'))

#key madum print

print(user.keys())

#value's madum print

print(user.values())

print("________________________________________")

#key and values 2num print panna

print(user.items())
print("________________________________________")

for x,y in user.items():
    print(x,":",y)
print("________________________________________")

for i in user.values():
    print(i)


for i in user.keys():
    print(i)
print("___________________________________")
#if condition
if "Age" in user:
    print("yes")


#changeing values
print(user)
print("------------------------------")
user.update({"genter":"mala"})
print(user)
user["Age"]=21
print(user)

user.pop("Age")
print(user)
print("----------------------------------------------------")
#del (user)
#print(user)
#user.clear()
#print(user)


print("============================================================================")

users={

"user1":{
    "name":"pranavamuthu",
    "Age":21,
    "marraide":False,
    "stutend":True
},
    "user2":{
    "name":"muthu",
    "Age":25,
    "marraide":False,
    "stutend":True
}



}
print(users)