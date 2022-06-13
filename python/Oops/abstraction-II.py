from abc import ABC, abstractmethod


class Animal(ABC):

    #concrete method
    def sleep(self):
        print("I am going to sleep in a while")

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
c.sleep()
c.sound()

c = Snake()
c.sound()


class Rabbit(Animal):
    def sound(self):
        super().sound()
        print("I can squeak")


c = Rabbit()
c.sound()
