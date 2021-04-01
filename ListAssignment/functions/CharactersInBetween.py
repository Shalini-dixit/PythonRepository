first_char=ord(input("enter a start character"))
last_char=ord(input("Enter an end character"))

for letter in range(first_char+1,last_char):
    print( chr(letter), end=" ")

