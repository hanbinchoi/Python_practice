import math

print('Result>')
side1=float(input('Enter the First side of a Triangle:'))
side2=float(input('Enter the Second side of a Triangle:'))
side3=float(input('Enter the Third side of a Triangle:'))
p=side1+side2+side3
s=p/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print()
print('The Perimeter of Triangle = {}'.format(p))
print('The Semi Perimeter of Triangle = {}'.format(s))
print('The Perimeter of Triangle = %.2f'%area)
