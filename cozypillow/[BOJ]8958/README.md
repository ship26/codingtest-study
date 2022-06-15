# 8958. OX퀴즈
[문제](https://www.acmicpc.net/problem/8958)

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

### 입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

```
# 입력 예시
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
```



### 출력
각 테스트 케이스마다 점수를 출력한다.

```
#출력 예시
10
9
7
55
30
```



### 풀이

이 문제를 풀기 위해 알아야 하는 스킬은 두 가지입니다.

1. 특정 문자열을 기준으로 문자열 처리하기
3. 등차수열 덧셈

문자열은 정규표현식을 이용해서, 등차수열 합은 range를 이용해서 구현했습니다. 

```python
import re

#케이스 수 입력
case = int(input())

# case 수 만큼 반복
for i in range(case):
    score = 0
    quiz = input()
    score_l = re.split(r'[*X]', quiz)
    for _ in score_l:
        score += sum(range(1,len(_)+1))
    print(score)
```