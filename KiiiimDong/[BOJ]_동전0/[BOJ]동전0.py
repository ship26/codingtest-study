import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin_list = []
count = 0
for i in range(n):
    coin_type = int(input())
    coin_list.append(coin_type)
coin_list = sorted(coin_list, reverse=True)
for coin in coin_list: # 오름차순 정렬된 것을 큰것부터 꺼낸다.
    if coin > k:
        pass
    else: 
        count += k // coin # 코인 갯수(몫) 카운트
        k = k % coin # 코인으로 나눈뒤의 k(나머지)를 갱신
print(count)