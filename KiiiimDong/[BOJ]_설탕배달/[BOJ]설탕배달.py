import sys
input = sys.stdin.readline
sugar = int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫 = 5의 가방의개수
        print(bag)
        break 
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
    # 입력이 3일때는 0 % 5==0 해서 if조건 만족되는게 계산안되고 밑에 sugar-=3하는 것만 bag+=1 돼서 1이 출력된다.
else:
    print(-1)