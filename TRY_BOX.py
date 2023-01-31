#Try block
try:
    a=10/0
except Exception as e:
    print(e)

#Try else block
try:
    a=10/3
except Exception as e:
    print(e)
else:
    print(a)

#finally block
#Try box
try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a)
finally:
    print("Hi")