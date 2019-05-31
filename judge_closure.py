def countdown(n):
    
    def minus():
        nonlocal n;
        n-=1
        return n+1;
    return minus

n=int(input())

c=countdown(n)

for i in range(n):
    print(c(),end=' ')
    
