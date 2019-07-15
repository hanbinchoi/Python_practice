def number_generator(start,stop):
    n=start

    while n<stop:
        if prime_number(n):
            
            yield n
        n+=1
        
def prime_number(number):
    for f in range(2,number):
        if number % f ==0:
            return False
    
    return True

def prime_number_generator(start,stop):
    yield from number_generator(start,stop)

start ,stop=map(int,input().split())

g=prime_number_generator(start,stop)
print(type(g))

for i in g:
    print(i,end=' ')
    
