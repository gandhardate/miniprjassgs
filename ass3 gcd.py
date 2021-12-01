def GCD(x, y):
    if x > y:
        small = y
    else:
        small = x
    for a in range(1, small+1):
        if((x % a == 0) and (y % a == 0)):
            GCD = a 
    return GCD

num1 = int(input("Enter Number 1: ")) 
num2 = int(input("Enter Number 2: ")) 

print("The G.C.D. is", GCD(num1, num2))
