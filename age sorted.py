name=['sk','pk','ok','tk','rk']
age=[78,56,23,45,22]
city=['pondy','cuddalore','goa','uk','us']
b=list(zip(age,name,city))
c=sorted(b)
s=1
for i in c:
  print("{}.{} age is {} ,living in {}".format(s,i[1],i[0],i[2]))
  s=s+1