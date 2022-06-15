# 2935. 소음
### [문제](https://www.acmicpc.net/problem/5355)

시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

### 입력
첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

```
# 입력 예시
100
```



### 출력
```
#출력 예시
A
```



### 풀이

```python
score = int(input())

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

```

조건문 기본 문제입니다.

말이 필요 없습니다..

근데 뇌까락 풀고 코드 치다가 한 번 틀렸습니다..^^