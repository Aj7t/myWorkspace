# from abc import ABC
import math

class shape:
    
    # atributes
    def __init__(self,name, l,b=None, r=None):
        self.l = l
        self.b = b
        self.r = r
        
    def calArea(self):
        if self.l and self.r is None:
            return math.pow(self.l,2)
        else:
            return (math.pi*(math.pow(self.l,2)))
        
        
        
# obj creation
rect = shape("rectangle", 10, 20)
print(rect.calArea())


sqr= shape("square",5)
print(sqr.calArea())

cir= shape("circle",10)
print(cir.calArea())