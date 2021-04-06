# 1. The computer will "think" of a 3 digit number that has no repeating digits
# 2. You will guess a 3 digit number
# 3. The computer will then give back clues, possible clues are:
 
# - Close: You have guessed the correct number but in the wrong position.
# - Match: You have guessed the correct number in the correct position.
# - Nope: You haven't guessed any of the numbers correctly.
 
# Based on these clues you will guess again until you break the code with a perfect match.
 
import random
 
def guessing(guess):
    int_guess= []
    for x in guess:
        int_guess.append(int(x))
 
    int_guess = int_guess[:3]
    # print(int_guess)
 
    found_match = 0
    found_close = 0
 
    for i in digits:
        for j in int_guess:
            if i == j:  # compare values
                # print("i and j:", i, j)
 
                if digits.index(i) == int_guess.index(j):
                    #print("Match")
                    found_match += 1
                else:
                    #print ("Close")
                    found_close += 1
            
    if found_match == 0 and found_close == 0:
        print("Nope")
 
    return(found_match == 3)
 
digits = list(range(10))
random.shuffle(digits)
#print(digits[:3])
digits = digits[:3]
print(digits)
 
my_guess = input("What is your guess? ")
while not guessing(my_guess): 
    my_guess = input("What is your guess? ")