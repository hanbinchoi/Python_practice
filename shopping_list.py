slist=[]

while True:
    element=input("Please enter what you want: ")
    if element=='quit':
        break;
    
    slist.append(element)
    slist.sort()
    for i,value in enumerate(slist):
        print(i+1,value)
        
