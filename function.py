def unpacking(name,age,address):
    print(name)
    print(age)
    print(address)

mydict={'name':'kim','age':22,'address':'seoul'}
unpacking(*mydict)
