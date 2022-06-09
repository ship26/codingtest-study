import sys
input = sys.stdin.readline
n = int(input())
time_list=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
time_list.sort() # 오름차순 정렬 앞에꺼기준으로
std = time_list[0] # 시작시간
count = 1
for i in range(1,n):
    if (std[1]-std[0]) > (time_list[i][1]-time_list[i][0]) and std[1]>time_list[i][1]: 
        # 시작시간 차가 종료시간 차보다 더크고, 시작시간이 이전타임의  종료시간보다 커야한다. 
        std=time_list[i]
    elif std[1]<=time_list[i][0]:
        count+=1
        std=time_list[i]
print(count)

## 간단풀이
import sys
input = sys.stdin.readline
n = int(input())
time = []

for _ in range(n):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j
print(conut)