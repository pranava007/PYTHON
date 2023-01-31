class employee:
    def workinghur(self):
        self.hrs = 50

    def printhurs(self):
        print("working hours :",self.hrs)

class trainee(employee):
    def workinghur(self):
        self.hrs = 60

Employe=employee()
Employe.workinghur()
Employe.printhurs()

Trainee=trainee()
Trainee.workinghur()
Trainee.printhurs()