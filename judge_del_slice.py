x=input().split()
del x[len(x):len(x)-6:-1]
print(tuple(x))
