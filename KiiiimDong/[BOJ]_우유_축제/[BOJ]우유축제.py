import sys
input = sys.stdin.readline
store_number = int(input()) # 우유 가게 개수
store_list = list(map(int,input().split())) # 우유 가게 들르는 순서
count = 0
last_number = 2 # 처음에 0이 들어가는데 무조건 마셔야 하기때문에 조건을 만족시키는 초기값 설정.
for i in range(store_number):
    if (store_list[i] == 0 and last_number == 2) or (store_list[i] == 1 and last_number == 0) or (store_list[i] == 2 and last_number == 1): 
        count += 1 # 카운트 해야할 조건
        last_number = store_list[i] # 최근에 마신 우유 갱신
    else:
        continue
print(count)



'''
for i in range(store_number):
    if store_list[i] == 0 and last_number == 2:
        count += 1
        last_number = store_list[i]
    elif store_list[i] == 1 and last_number == 0:
        count += 1
        last_number = store_list[i]
    elif store_list[i] == 2 and last_number == 1:
        count += 1
        last_number = store_list[i]
    else:
        continue
print(count)
'''