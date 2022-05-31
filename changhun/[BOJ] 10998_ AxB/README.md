# AxB

문제링크 : https://www.acmicpc.net/problem/10998

## 문제

두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력 

첫째 줄에 A×B를 출력한다.

```python
A,B = map(int,input().split())
print(A-B)
```

map 함수를 통해 input받는 값을 int로 받게끔 값을 매기는 방식으로 표현해봤습니다.

```python
A,B = input().split()
print(int(A)*int(B))
```

print문에서 A, B의 값을 int로 변경하여 연산하는 방식 또한 적어봤습니다.