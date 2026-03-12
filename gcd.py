a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
while b != 0:
    rem=a%b
    a=b
    b=rem
print("the gcd is",a)