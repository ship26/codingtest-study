import sys
input = sys.stdin.readline
n = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list)
fake_list = []
for i in range(n):
    fake_list.append(score_list[i]/max_score*100)
print(sum(fake_list)/n)
