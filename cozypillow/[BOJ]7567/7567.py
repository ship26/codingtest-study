bowls = input()
h = 10

for i in range(1,len(bowls)):
    if bowls[i] == bowls[i-1]:
        h += 5
    else:
        h += 10

print(h)