a,b=map(int,input().split())
x=[]
for i in range(a,b+1):
    if i==a+1 or i==b-1:
        continue
    x.append(pow(2,i))

print(x)
    
