import sys
input = sys.stdin.readline

n = int(input())
cnt = {1:0}
for i in range(2, n+1):
    if i % 3 == 0:
        cnt[i] = cnt[i//3] + 1
    if i % 2 == 0:
        if i in cnt:
            cnt[i] = min(cnt[i], cnt[i//2] + 1)
        else:
            cnt[i] = cnt[i//2] + 1
    if i in cnt:
        cnt[i] = min(cnt[i], cnt[i-1] + 1)
    else:
        cnt[i] = cnt[i-1]+1
        
print(cnt[n])
