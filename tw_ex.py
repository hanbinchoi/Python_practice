voted={'john':'True','alice':'False','rosa':'True'}
print(voted)

while True:
    name = input('Enter your name : ')
    if name=='':
        print('quit')
        break
    if voted.get(name)==True:
        print(name,' already voted!')
    elif voted.get(name)==False:
        print(name,', please vote!')
        voted[name]=True
    else:
        print(name,'has no voting rights.')


print(voted)
