import sys
input = sys.stdin.readline

v, e = map(int, input().split())
ev = []
for _ in range(e):
    ev.append(list(map(int, input().split())))
    ev[-1][0] -= 1
    ev[-1][1] -= 1
ev.sort(key=lambda x: x[2])
uniind = [-1] * v
ans = 0

for i in ev:
    if i[0] == i[1]:
        continue
    if uniind[i[0]] == -1 and uniind[i[1]] == -1:
        if i[0] < i[1]:
            uniind[i[1]] = i[0]
            uniind[i[0]] = i[0]
        else:
            uniind[i[0]] = i[1]
            uniind[i[1]] = i[1]
    elif uniind[i[0]] == uniind[i[1]]:
        continue
    elif uniind[i[0]] == -1:
        uniind[i[0]] = uniind[i[1]]
    elif uniind[i[1]] == -1:
        uniind[i[1]] = uniind[i[0]]
    else:
        childnode = i[0]
        tmp = uniind[childnode]
        while tmp != uniind[tmp]:
            uniind[childnode] = uniind[tmp]
            tmp = uniind[tmp]
        childnode = i[1]
        tmp = uniind[childnode]
        while tmp != uniind[tmp]:
            uniind[childnode] = uniind[tmp]
            tmp = uniind[tmp]
        if uniind[i[0]] == uniind[i[1]]:
            continue
        if uniind[i[0]] < uniind[i[1]]:
            tmp = uniind[i[1]]
            uniind[tmp] = uniind[i[0]]
            uniind[i[1]] = uniind[i[0]]
        else:
            tmp = uniind[i[0]]
            uniind[tmp] = uniind[i[1]]
            uniind[i[0]] = uniind[i[1]]
    ans += i[2]
print(ans)