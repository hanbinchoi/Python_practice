x={i for i in range(0,101) if i%3==0}
y={i for i in range(0,101) if i%5==0}
print(x)
print(y)
print(x.intersection(y))
print(sorted(x.intersection(y)))
