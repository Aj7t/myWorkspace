
class animals:
    # Instance attribute
    def __init__(myObj,name,age,color):
        myObj.name=name
        myObj.age=age
        myObj.color=color

    #methods
    def eat(myObj):
        print(myObj.name + " is eating")
    def sleep(myObj):
        print(myObj.name + " is sleeping")
    def walk(myObj):
        print(myObj.name + " is walking")
    def speak(myObj):
        print(myObj.name + " is speaking")
        
        
    def about(myObj):
        return myObj.name + " is " + str(myObj.age) + " years old"



#main function
    
# baseClass object creation
myobj1 = animals("Rocky", 2, "brown")
myobj1.eat()
myobj1.age = 10
# del myobj1
print(myobj1.about())

