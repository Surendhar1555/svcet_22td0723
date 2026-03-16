amt = int(input("amt: "))
coins = [500,200,100,50,20,10,5,2,1]
for c in coins:
    if(amt>=c):
      count=amt//c
      amt=amt%c
      print("{} x {}".format(c,count))