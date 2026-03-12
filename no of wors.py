a = input("enter paragraph: ")
c = 0
p = " "
for i in a:
    if(i!= " " and p== " "):
        c = c + 1
    p = i
print(c)