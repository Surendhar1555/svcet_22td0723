name=['sk','pk','ok','tk','rk']
mark=[[30,40,50],[78,37,56],[48,15,48],[98,78,64],[12,87,49]]
for i in range(5):
  pr=sum(mark[i])//3
  if(pr>90):
    g='s'
  elif(pr>60 and pr<90):
    g='a'
  elif(pr>40 and pr<60):
    g='b'
  else:
    g='f'
  print("{}.{}-{}".format(i+1,name[i],pr,g))