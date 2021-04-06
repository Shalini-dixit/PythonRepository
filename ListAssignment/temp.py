import random,sys
LENGTH =3

def guessing(comp_choice,user_choice):
    #print("computer ",comp_choice)
    #print("user choice", user_choice)
    match_score=0
    close_score=0

    comp_choice = str(comp_choice)
    for i in range(LENGTH):
        for j in range(LENGTH):
            if comp_choice[i]==user_choice[j]:
                if i==j:
                    match_score +=1
                else:
                    close_score +=1
   
    if (match_score==LENGTH):
        print("Match")
        sys.exit()
    else: 
        if close_score==LENGTH:
            print("Close")
        elif close_score==2 and match_score ==1:
            print("Close")
        else:
            print("Nope")

        user_choice=input("Again enter your choice, three digit number")
        guessing(comp_choice, user_choice)
            

def generateComputerChoice():
    comp_choice =""
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    digits = digits[:3]
    for x in digits:
        comp_choice = comp_choice+x
    return comp_choice

    
def generateUserChoice():
    user_choice= input("enter your choice, three digit number")
    if len(user_choice)!=3: 
        print("Program terminated, your choice must be a three digit number")
        sys.exit()
    return user_choice

def main():
    guessing(generateComputerChoice(),generateUserChoice())

main()
