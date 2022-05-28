import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))

start = 0
end = 1
cnt = 0

while end <= n and start <= end:
    sum_num = num[start:end]
    tot = sum(sum_num)

    if tot == m:
        cnt += 1
        end += 1

    elif tot < m:
        end += 1

    else:
        start += 1

print(cnt)
