import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
ev = [i for i in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    while ev[a] != a:
        a = ev[a]
    while ev[b] != b:
        b = ev[b]
    if ev[a] < ev[b]:
        ev[b] = ev[a]
    else:
        ev[a] = ev[b]

ans = 0
for i in range(1, n):
    j = i
    while ev[j] != j:
        j = ev[j]
    if j == 0:
        ans+=1
print(ans)