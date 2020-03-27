a=int(input('Enter number: '))
count=1
while True:
    if a//10==0:
        break;
    else:
        a=a/10
        
    count=count+1

print('The number of digits in the number is : ',count)
