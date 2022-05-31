# 사칙연산

문제링크 : https://www.acmicpc.net/problem/10869

## 문제

두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 

## 입력

두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

## 출력 

첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

```python
A,B = map(int,input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)
```

map 함수를 통해 input받는 값을 int로 받게끔 값을 매기는 방식으로 표현해봤습니다.
각 출력문에 사칙연산 값을 출력하도록 했습니다.