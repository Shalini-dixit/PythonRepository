def passwordValidation(password):
    password_length=len(password)
    digit_counter=0
    returnStr =""
    flag = False

    if password_length<6 or password_length>10:
        returnStr += "Password must be between 6 and 10 characters. "
    
    for x in password:
        x=ord(x)
        if (x>=ord('0') and x<=ord('9')):
            digit_counter += 1
        if   flag == False and not ((x>=ord('0') and x<=ord('9')) or (x>=ord('a') and x<=ord('z')) or (x>=ord('A') and x<=ord('Z'))):
            flag=True
            returnStr += "Password must consist only of letters and digits. "
            
    if digit_counter<2:
        returnStr = returnStr + "Password must have at least 2 digits. "

    if len(returnStr)<1:
        return "Passwordisvalid"
    else:
         return returnStr

pswrd_string ="logIn"
print(pswrd_string)
print(passwordValidation(pswrd_string))
print("---------------------------------------")
pswrd_string="MyPass123"
print(pswrd_string)
print(passwordValidation(pswrd_string))
print("---------------------------------------")
pswrd_string="Pa$s$s"
print(pswrd_string)
print(passwordValidation(pswrd_string))
print("---------------------------------------")