# Mini prj assignment 1
# Factorial of non-negative number
print("Enter a number: ")
num = int(input())
if num < 0:
    print("Invalid input\n")
elif num == 0 or num == 1:
    print("The factorial is: 1\n")
else:
    fact = 1
    while(num > 1):
        fact *= num
        num -= 1
    print("The factorial is: "+str(fact)+"\n")

