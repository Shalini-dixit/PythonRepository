total_ppl = int(input("Enter total number of people "))
capacity = int(input("enter capacity of elevator "))
courses =0

if total_ppl%capacity != 0 :
    courses=courses+1

courses = courses + (total_ppl//capacity) 
print(courses)