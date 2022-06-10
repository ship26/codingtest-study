import sys

input = sys.stdin.readline

N = int(input())
treedict = {}
for _ in range(N):
    a = input().split()
    treedict[a[0]] = a[1:]

stk = []
output = [[], [], []]

stk.append(['A', 0])
while stk:
    cur = stk[-1]
    if cur[1] < 2:
        if treedict[cur[0]][cur[1]] != '.':
            stk.append([treedict[cur[0]][cur[1]], 0])
        if cur[1] == 0:
            output[0].append(cur[0])
        else:
            output[1].append(cur[0])
    else:
        output[2].append(cur[0])
        stk.pop()
        continue
    cur[1] += 1

for i in output:
    print(''.join(i))