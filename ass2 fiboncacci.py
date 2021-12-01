# miniprj assignment 2
# Write a program to find fibonacci series using recurrsion 

def fibo(a):  
   if a <= 1:  
       return a  
   else:  
       return(fibo(a-1) + fibo(a-2))  

no_terms = int(input("Enter the no. of terms you want to display: "))  
  
if no_terms <= 0:  
   print("Please enter a positive integer no.")  
else:  
   print("Fibonacci sequence: ")  
   for y in range(no_terms):  
       print(fibo(y))
