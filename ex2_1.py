import math

print('Result>')
radius=int(input('Please Enter the Radius of a Cylinder:'))
height=int(input('Please Enter the Height of a Cylinder:'))
volume=math.pi*radius**2*height
area=(2*math.pi*radius**2)+(2*math.pi*radius*height)
print("\n The Surface Area of a Cylinder = {}".format(area))
print(" The Volume of a Cylinder = {}".format(volume))


