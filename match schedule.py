import random
n = int(input("Enter number of teams: "))
teams=[]
for i in range(n):
    name=input("Enter team {}: ".format(i+1))
    teams.append(name)
meet = int(input("No of meets: "))

matches = []
for i in range(n - 1):
    for j in range(i + 1, n):
        for k in range(meet):
            matches.append([teams[i],teams[j]])

random.shuffle(matches)
pos = 1
for i in matches:
    print("Match {}: {} vs {}".format(pos,i[0],i[1]))
    pos += 1