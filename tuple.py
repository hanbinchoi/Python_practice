tu=('apple',[7,5,6],(1,2,3))
tu[2][0]=8
print('original: tu = ',tu)

li=list(tu)

print('casting: li = ',li)


tu2=tuple(li)

print('conveted tuple: tu2 = ',tu2)

tu2[1][1]=20

print('tu2[1][1]=20, result: ',tu2)


tu2[1][2]=sum(tu2[1][0:2])

print('tu2[1][0:2], result: ',tu2)
