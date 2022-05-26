# 2798. 블랙잭
### [문제](https://www.acmicpc.net/problem/2798)
카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다. 블랙잭은 카지노마다 다양한 규정이 있다.

한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.

김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다. 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

### 입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.

합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

### 출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

### 풀이

![순열공식](permutation.jpg)

이 문제는 세 단계를 거쳐 풀었습니다.

1. 3개의 수를 더한 모든 경우의 수를 생성하고
2. 숫자를 정렬하고
3. M과 가장 가까운 수를 찾는 문제입니다.


솔직히 저한테는 너무 어려워서 경우의 수 생성하는 코드는 오래 고민하다가 [구글링](https://velog.io/@jeongdopark/Algorithm-python-%EB%B0%B1%EC%A4%80-2798%EB%B2%88)했습니다. 어떻게 반복문으로 하면 될 것 같은데 떠오르질 않았습니다. 코드 구현의 문제라기보다는 산수를 못해서요...ㅜㅜ 모르는 문제 포기하기보단 찾아보는 편이 낫죠..?

경우의 수 관련 내용을 찾다가 **itertools**라는 패키지를 알게됐습니다. 반복작업을 편하게 만들어주는 패키지인 모양입니다. itertools 안에 있는 Permutation을 이용하면 중복 없는 경우의 수를 생성할 수 있다고 합니다. 
이 itertools에 대해 알아두면 여러모로 쓸모가 많을 것 같아 정보를 공유합니다.

```
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

num_list = set(num_list) # 중복제거
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

```