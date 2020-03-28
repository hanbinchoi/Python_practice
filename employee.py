class Employee:
    
    count=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.count+=1
    def getSalary(self):
        return self.salary
    
    def getName(self):
        return self.name

    def getCount():
        return Employee.count


kim=Employee('Kim',2000)


print('Result:')

print("{}'s salary is {}".format(kim.getName(),kim.getSalary()))
print('Total employee count:',Employee.getCount())

lee=Employee('Lee',3000)
print("{}'s salary is {}".format(lee.getName(),lee.getSalary()))
print('Total employee count:',Employee.getCount())
