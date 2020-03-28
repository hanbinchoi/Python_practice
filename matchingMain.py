from matching import *
import time

list1=[]
list2=[]

a=input('data list(ex:a,b,c): ')

b=input('data list(ex:a,b,c): ')

list1=dataInput(a)
list2=dataInput(b)


print('shake for 3 seconds...')
time.sleep(3)
list1=shake(list1)
list2=shake(list2)

print('congratulations~~~')

for i in range(3):
    print(list1[i],'<------------>',list2[i])
    

