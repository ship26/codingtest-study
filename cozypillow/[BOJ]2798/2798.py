# 입력단
N, M = map(int, input().split())
cards = list(map(int,input().split()))
num_list = []
result = 0

# 연산
for i in range(0, len(cards)-2):
    for j in range(i+1, len(cards)-1):
        for k in range(j+1, len(cards)):
            num = cards[i] + cards[j] + cards[k]
            num_list.append(num)

num_list = set(num_list)
num_list = sorted(num_list)

for num in num_list:
    if num == M:
        result = num
        break
    elif num > M:
        break
    elif num > result:
        result = num
        
# 출력단
print(result)
