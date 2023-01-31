a=[10,3,4,5,6,7]
print(a[0])
#mutable === value change pannalam
a[0]=20
print(a[0])
print(a)
#revelse
print(a[-2])
#partickular range ckula varum
print(a[1:3])
print(a[1:-1])
#full print first eruthu
print(a[1:])
#full end eruthu first var print
print(a[:5])
#all type date run the list
a=['a',2,True,"muthu",2.3,[1,2,3,4,5]] #nested list
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(type(a[4]))
print(type(a[5]))
print(a[5])
print("what ",a[5][0])  # list ula erucka list oda value index number vache find out pantrathu
a = [1,2,3,4,5]
print(a)
a.clear() # totaly clear
print(a)
a = [1,2,3,4,5]
b=a.copy() #totaly copy move to onather one
a.clear() # total clear
print(b)
print(a)
a =[2,27,3,544,5,55] #athana thada va vathurucku
print(a.count(5))
print(a.index(2)) #index value
print(len(a)) #lenth find out
print(max(a)) # eruckurathula high
print(min(a)) # eruckurathula low
print(a)
a.pop(0) # index vache remove pannurathu
print( "pop why",a)
a.remove(544) #value vachee remove pandrathu
print(a)
name = ["pranava"] # oru list ula new va name add pannurathu
print(name)
name.append("muthu")
name.append("yamuna")
name.append(" baby shiva")
print(name)
name2 =["cool","mass","focuse"] #2 list join pandrathu
name.extend(name2)
print(name)
name.insert(0,"yamuna") #index vachee new name add pandrathu
print(name)
print(list(range(5))) #constructor loop function mari
a=[20,50,70,100,30,10]
a.sort() #ascending
print(a)
a.sort(reverse=True)#descending
print(a)
a=["oragen","apply","cost"]
a.sort() #ascending
print(a)
a.sort(reverse=True)#descending
print(a)
a=["oragen","apply","cost","pranavamuthu"]
a.sort(key=len) #ascending
print(a)






