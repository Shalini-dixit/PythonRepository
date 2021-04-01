def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def add_and_subtract(num1, num2, num3):
    temp=add(num1,num2)
    return subtract(temp,num3)

print(add_and_subtract(23,6,10))
print(add_and_subtract(1,17,30))
print(add_and_subtract(42,58,100))