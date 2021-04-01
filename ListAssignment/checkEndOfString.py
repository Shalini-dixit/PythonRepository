def chkEndOfString(str1, str2):
    
    if len(str1)<len(str2):
        big_str=str2.lower()
        sub_str=str1.lower()
    else:
        big_str=str1.lower()
        sub_str=str2.lower()
    
    for x in range(-len(sub_str),0):
        if big_str[x]!=sub_str[x]:
            return False
        else:
            break
    return True

print(chkEndOfString("abC","styabc"))
print(chkEndOfString("abCz","styabc"))
print(chkEndOfString("abc","Hiaba"))
    
    


