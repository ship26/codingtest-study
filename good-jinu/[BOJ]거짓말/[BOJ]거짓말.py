import sys
from collections import deque
input = sys.stdin.readline

def f():
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        return M

    que = deque()
    # 거짓말하면 안되는 사람 리스트 (블랙 리스트)
    blk_l = [False] * N
    for i in tmp[1:]:
        blk_l[i - 1] = True
        que.append(i - 1)
    # 각 파티에 참가하는 사람들 리스트
    people_l = []
    # 각 사람들이 참가하는 파티 리스트
    party_l = [[] for _ in range(N)]
    for i in range(M):
        tmp = list(map(lambda x: int(x) - 1, input().split()))[1:]
        for j in tmp:
            party_l[j].append(i)
        people_l.append(tmp)
    # 블랙리스트의 사람이 참석한 파티 리스트 (거짓말을 하면 안되는 파티)
    blk_party = []
    while que:
        person = que.popleft()
        for i in party_l[person]:
            if i not in blk_party:
                blk_party.append(i)
                for j in people_l[i]:
                    if not blk_l[j]:
                        blk_l[j] = True
                        que.append(j)
    return M - len(blk_party)

print(f())