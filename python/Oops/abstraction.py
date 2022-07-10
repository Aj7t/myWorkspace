
# abstract base class work
from abc import ABC, abstractmethod


class animals(ABC):
    
    @abstractmethod
    def colour(myObj):
        pass
    

class Dog(animals):
    def colour(myObj):
        print("The Dog colour is white")


class Cat(animals):
    def colour(myObj):
        print("The Cat colour is black ")


class lion(animals):
    def colour(myObj):
        print("The lion colour is yellow ")



# Driver code
D = Dog()
D.colour()

C = Cat()
C.colour()

L = lion()
L.colour()
