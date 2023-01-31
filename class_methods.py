class student:
    name="pranavamuthu"
    age=21
    gender="male"

    def printall():
        print(student.name)
        print(student.age)
        print(student.gender)
#one mothed
student.printall() #all devalper use best mothed
#2nd mothed
getattr(student,"printall")()
#3thd mothed
student.__dict__['printall']()