class student():
    name="muthu"
    age=21
    education="MCA"
#getattr mothed
print(getattr(student,"name"))
print(getattr(student,"age"))
print(getattr(student,"education"))
#add new attributes
setattr(student,"genter","male")
print(student.genter)
#Dot mothed
print(student.name)
print(student.age)
print(student.education)
#add new attributes
student.mark=20
print(student.mark)
#delete
delattr(student,"mark")
print(student.__dict__)


student.mark=20
print(student.mark)
del student.mark
print(student.__dict__)
