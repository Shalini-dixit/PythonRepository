
MyStr=input("Enter space seperated integer values")
NewList=[]

for x in MyStr.split(' '):
    NewList.append(- int(x))

print(NewList)