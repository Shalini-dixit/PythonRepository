n= int(input("Enter the size of triples"))
total =0
for i in range(97,97+n):
    for j in range(97,97+n):
        for k in range(97,97+n):
            print(chr(i)+ chr(j)+ chr(k))
            total = total+1

print("Total number of triplets: ", total)
    