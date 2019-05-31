import string

aList=input().split()
count=0
for i in aList:
    word=i.strip(string.punctuation+' ')
    if(word=='the'):
        count+=1
print(count)
