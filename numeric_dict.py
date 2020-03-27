engdict={'1':'one','2':'two','3':'three','4':'four','5':'five'}
spandict={'1':'uno','2':'dos','3':'trois','4':'cuatro','5':'cinq'}
frendict={'1':'un(e)','2':'deux','3':'tres','4':'quatre','5':'cinco'}
title=('English','Spanish','French')
while True:
    a=input('Please enter a number (1~5): ')

    if a=='':
        break
    print(title[0],':',engdict[a])
    print(title[1],':',spandict[a])
    print(title[2],':',frendict[a])

