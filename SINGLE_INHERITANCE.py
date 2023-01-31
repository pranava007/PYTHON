class nokiya:
    company="nokiya"
    wbesite="www.nokiya.com"

    def company_address(self):
        print("sapanoor roda ,palaya valavu,kallal pincode=630305")

class nackiya007(nokiya):

    def __init__(self):
        self.name="moblie007"
        self.year="1990"

    def product_ditailes(self):
        print("Name :",self.name)
        print("Year : ",self.year)
        print("company :",self.company)
        print("wbesite :",self.wbesite)

moblie = nackiya007()
moblie.product_ditailes()
moblie.company_address()


