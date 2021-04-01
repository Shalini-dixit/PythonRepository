digits="3495892137259234"

def SumOfOddEvenDigits(num):
    sum_even=0
    sum_odd=0
    for digit in digits:
        digit=int(digit)
        if(digit%2==0):
            sum_even += digit
        else:
            sum_odd += digit
    return "Odd sum : {} ; Even Sum : {} ".format(sum_odd,sum_even)

print(SumOfOddEvenDigits(digits))
