a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))
c=int(input("enter 3rd number: "))
a1=[int(i) for i in str(a)]
b1=[int(i) for i in str(c)]
c1=[int(i) for i in str(a)]

large=max(a1)+max(b1)+max(c1)
small=min(a1)+min(b1)+min(c1)

print("key is ",large*small)