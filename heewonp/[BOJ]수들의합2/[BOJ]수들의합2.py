import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))

start = 0
end = 0
cnt = 0
sum = 0


while True:
    if sum >= m:
        if sum == m:
            cnt += 1
        

print(cnt)
