def sq():
    s=int(input("enter Side of sq: "))
    print("area of square: ",s*s)
    
def rec(l,b):
    print("area of rect: ",l*b)
    
def tri():
    b=int(input("enter breadth:"))
    h=int(input("enter height:"))
    return 0.5*b*h
    
def cir():
    r=int(input("enter radius: "))
    return 3.14*r*r
    
ch=0
while (ch!=5):
    print("1.Square")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Circle")
    print("5.Exit")
    print()

    ch = int(input("Enter choice: "))
    if(ch==1):
        sq()

    elif(ch==2):
        l = int(input("enter length: "))
        b = int(input("enter breadth: "))
        rec(l,b)
        print()

    elif(ch==3):
        print("area of triangle:", tri())
        print()

    elif(ch==4):
        print("area of circle:", cir())
        print()

    elif(ch==5):
         print("Tata Bye")
         print()
    
    else:
        print("Waste of time")
        print()