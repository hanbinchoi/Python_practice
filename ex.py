num = int(input('Enter number: '))

count=0
print('Reverse of the number : ',end='')
while num>0:
    print(num%10,end='')
    num //= 10

