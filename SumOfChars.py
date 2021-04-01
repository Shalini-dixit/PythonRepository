import sys

num_char=int(input("How many characters you want to sum up between 1 to 20 : "))
if num_char < 1 or num_char > 20 :
    print("Out of range")
    sys.exit()

sum = 0
for i in range(num_char):
    char = ord(input("enter a valid english character(A-Z, a-z)"))
    if (char>=65 and char<=90) or (char>= 97 and char<=122):
       sum = sum+char

    else:
        print("Invalid character")
        sys.exit()

print(sum)