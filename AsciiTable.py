indx_frst=int(input("Input ASCII code of first character of Ascii table"))
indx_last=int(input("Input ASCII code of last character of Ascii table"))

for x in range(indx_frst, indx_last+1):
    print(chr(x))
