import sys 
input = sys.stdin.readline
n = int(input())
P_list = sorted(list(map(int, input().split()))) # 오름차순정렬
time = []
for i in range(n):
    time.append(sum(P_list[:i+1])) # P_list에서 처음부터 i까지 더한것을 리스트에 넣기
total_time = sum(time) # 리스트의 합
print(total_time)