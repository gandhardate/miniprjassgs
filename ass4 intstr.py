
# mini-project assignment 4

def function(n,base):
   convert_str = "0123456789ABCDEF"
   if n < base:
      return convert_str[n]
   else:
      return function(n//base,base) + convert_str[n % base]

x = int(input("Enter a number: "))
y = int(input("Enter the base: "))
print(function(x,y))
