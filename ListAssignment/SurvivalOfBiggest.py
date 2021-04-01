myText= input("Enter space seperated numbers")
n=int(input("Enter how many values you want to remove"))

myLists = myText.split(' ')
myLists.sort(reverse=True)

for x in range(n):
    myLists.pop()
print(myLists)