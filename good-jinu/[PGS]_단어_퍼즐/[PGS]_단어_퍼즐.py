from collections import deque

def solution(strs, t):
    strs = set(strs)
    mem = [len(t)+1] * len(t) # 문자열의 n번째 문자까지 필요한 최소 단어 조각의 수 (메모이제이션)
    q = deque()
    q.append((0, 0)) # (n번째 문자의 인덱스, 사용한 단어개수)
    while q:
        counts = q.popleft()
        scr = counts[1] + 1 # 단어 한개 추가
        end_i = counts[0] + 5 if len(t) - counts[0] >= 5 else len(t)
        for i in range(counts[0], end_i):
            if t[counts[0]:i + 1] in strs and mem[i] > scr:
                if i + 1 == len(t): # t의 끝에 도착했다면 사용한 최소 단어개수 반환
                    return scr
                q.append((i + 1, scr))
                mem[i] = scr
    return -1