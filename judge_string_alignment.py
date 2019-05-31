aList=list(map(int,input().split(';')))
aList.sort(reverse=True)
j=0
for i in aList:
    print('%9s'% format(aList[j],','))
    j+=1

    
