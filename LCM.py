a=int(input('Enter the First Value: '))
b=int(input('Enter the Second Value: '))

if a>b:
    max=a
else:
    max=b

 while True:
    if max%a==0 and max%b==0:
        print('LCM of {0} and {1} = {2}'.format(a,b,max))
        break;

    max=max+1
