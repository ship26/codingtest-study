import sys
from collections import deque
input = sys.stdin.readline

INF = 128
N, M = map(int, input().split())
relationship = [[INF] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    relationship[a - 1][b - 1] = 1
    relationship[b - 1][a - 1] = 1
for i in range(N):
    relationship[i][i] = 0
que = deque()
for i in range(N):
    for j in range(N):
        if i != j and relationship[i][j] < INF:
            que.append((j, relationship[i][j]))
    while que:
        pos = que.popleft()
        for j in range(N):
            if relationship[pos[0]][j] + pos[1] < relationship[i][j]:
                relationship[i][j] = relationship[pos[0]][j] + pos[1]
                que.append((j, relationship[i][j]))
total_score = list(map(lambda x: sum(x), relationship))
print(total_score.index(min(total_score)) + 1)