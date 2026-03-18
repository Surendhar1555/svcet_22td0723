n = int(input("Enter number of player: "))
players = []
gender = []

for i in range(n):
    x = input("Enter player name: ")
    y = input("Enter player gender: ")
    players.append(x)
    gender.append(y)

team = []
for i in range(n - 1):
    for j in range(i + 1, n):
        if(gender[i]!=gender[j]):
            team.append([players[i], players[j]])

print(team)