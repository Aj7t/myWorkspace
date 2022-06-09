from main import*

class rocky(animals):
    def __init__(self, name, age,color):
        super().__init__(name, age,color)
        self.birthYear = 2019

    def about(myObj):
        return myObj.name + " is " + str(myObj.age) + " years old"

class leo(rocky):
    pass

class teddy(rocky):
    def __init__(self, name, age,color):
        super().__init__(name, age,color)
        print("this is multilevel inheritance")

class bats(teddy,leo):
    def __init__(self, name, age,color):
        super().__init__(name, age,color)
        print("This is multiple inheritance")


#simple inheritence
myobj2 = rocky("Mike", 12, "brown")
print(myobj2.about())
print(myobj2.name , " BirthYear is " , myobj2.birthYear)

# multilevel inheritance
myobj3 = teddy("teddy", 20,"brown")
print(myobj3.about())

# multiple inheritance
myobj4 = bats("bats",12,"brown")
print(myobj4.about())
print(animals.mro())
