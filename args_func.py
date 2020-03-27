def func_sum(*args):
    total=0
    for i in args:
        total+=i
        
    return total

score=[73,95,80,57,99]
total=func_sum(*score)
print('Result>')
print('total score: ',total)
print('average score: ',total/len(score))
