a=int(input('Enter a number: '))
print('Reverse of the number: ',end='')
while True:
    digit=a%10

    print(digit,end='')
    if a//10==0:
        break
    a=a//10
