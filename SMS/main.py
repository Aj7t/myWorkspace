
#sms = student management system 

class sms:
    def __init__(self, name,role, rollNo, standard):
        self.name = name
        self.standard = standard
        self.role = role
        self.rollNo = rollNo

    #methods
    def result(self):
        print("result: %s" % self.name)

    def getfeeDetails(self):
        if self.standard <0 or self.standard >12:
            print("Please enter valid self.standard: %s" % self.self.standard)
        elif self.standard > 0 and self.standard <5 :
            print(self.name+  " " + " your fee is 10,000 only ")

        elif self.standard > 5 and self.standard <10 :
            print(self.name +  " " + "your fee is 20,000 only ")   
        else :
            print(self.name +  " " + "your fee is 50,000 only ")

    def about(self):
        return self.name +  " " + " is a " + self.role + " of our school"

    def details(self):
        return self.name + " " + self.role + " " + self.standard + " " + self.getfeeDetails() + " " + self.result + " " + self.rollNo



#main func 


ajit = sms("ajit", "student",6 )
print(ajit.about())
print(ajit.getfeeDetails()) 