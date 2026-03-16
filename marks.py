name=['sk','pk','ok','tk','rk','mk']
mark=['20','56','48','64','12','89']
dept=['cse','cse','ece','mech','it','mech']
s=1
for i in range(6):
  if int(mark[i])>40:
    print("{}.{} form {} has scored {}%".format(s,name[i],dept[i],mark[i]))
    s=s+1