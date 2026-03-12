n=int(input("Enter the num: "))
if(n%2==0):
    for i in range(1,11):
        print(f"{i}x{n}={i*n}")
else:
    for i in range(1,16):
        print(f"{i}x{n}={i*n}")