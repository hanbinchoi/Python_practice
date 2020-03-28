import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def cCircumf(self):
        return 2*math.pi*self.radius

    def cArea(self):
        return math.pi*self.radius**2

radi=int(input('enter radius: '))
c1=Circle(radi)
print(c1.cCircumf())
print(c1.cArea())


    
