import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N = int(input())
table = [{} for _ in range(N)]
for _ in range(N):
    a = list(map(int, input().split()))[:-1]
    for i in range(1, len(a), 2):
        table[a[0] - 1][a[i] - 1] = a[i + 1]
    if len(a) == 3: # 트리의 말단 노드 leaf에 저장
        leaf = a[0] - 1

q = deque()
max_dst = 0 # 결과 값 저장하는 변수
for _ in range(2):
    # 큐에 (노드번호, 간선 가중치) 삽입
    q.append((list(table[leaf].keys())[0], list(table[leaf].values())[0]))

    # visited 초기화
    visited = [-1] * N
    visited[leaf] = 0
    visited[q[0][0]] = q[0][1]
    while q: # BFS로 다른 모든 노드로의 거리 계산
        a = q.popleft()
        for i in table[a[0]]:
            if visited[i] == -1 or visited[i] > table[a[0]][i] + a[1]:
                q.append((i, table[a[0]][i] + a[1]))
                visited[i] = q[-1][1]
    
    # 가장 거리가 먼 노드의 인덱스와 거리값을 저장
    for i in range(len(visited)):
        if visited[i] > max_dst:
            max_dst = visited[i]
            leaf = i
print(max_dst)