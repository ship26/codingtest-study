# 두 수 비교하기

문제링크 : https://www.acmicpc.net/problem/1330

## 문제

두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

## 입력

첫째 줄에 A와 B가 주어진다. A와 B는 공백 한 칸으로 구분되어져 있다.

## 출력 

첫째 줄에 다음 세 가지 중 하나를 출력한다.

- A가 B보다 큰 경우에는 '>'를 출력한다.
- A가 B보다 작은 경우에는 '<'를 출력한다.
- A와 B가 같은 경우에는 '=='를 출력한다.

## 제한

- -10,000 ≤ A, B ≤ 10,000


```python
A, B = input().split()

if int(A) < int(B):
    print("<")
elif int(A) > int(B):
    print(">")
elif int(A) == int(B):
    print("==")
```

A B로 input을 받은 후 공백 구분이므로 .split()을 써줍니다. 비교를 위해 if와 elif 를 썼습니다. 
input의 리턴 값은 문자열이므로, int를 통해 정수형으로 바꿔주지 않으면 두 자리 숫자를 더 높은 값으로 인식하지 못하는 것을 뒤늦게 알아채서 A, B에 int 값을 지정했습니다.

```python
A, B = map(int,input().split())

if int(A) < int(B):
    print("<")
elif int(A) > int(B):
    print(">")
else:
    print("==")
```

map을 써서 input을 받을 때 A, B 각각의 값을 정수형으로 받도록 하는 법을 다른 사람의 코드를 보고 배웠습니다.
그리고 else문의 경우, 위 if문에 전부 해당하지 않는 (동일한 값) 경우에 출력되다보니 별도로 A, B에 대한 값을 적지 않아도 된다는 점 또한 배웠습니다.