from abc import ABC, abstractmethod

# Important thing is– you cannot create an object for the abstract class with the abstract method.
class Animal(ABC):

    #concrete method
    def family(self):
        print("hey we belong to animal family")

    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")
        pass
 
class Snake(Animal):
    def sound(self):
        print("I can hiss")
 
class Dog(Animal):
    def sound(self):
        print("I can bark")
 
class Lion(Animal):
    def sound(self):
        print("I can roar")
       
class Cat(Animal):
    def sound(self):
        print("I can meow")
        
        
c = Cat()
c.sound()

c = Snake()
c.sound()


class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")


c = Rabbit()
c.sound()
