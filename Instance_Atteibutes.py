class user:
    course="pytho"
print(user.course)


#print(user.__dict__)
o=user()
o.course
print(o.course)
#instance atteibutes
o.course="c++"
print(o.course)
print(o.__dict__)


