# [비밀번호 찾기](https://www.acmicpc.net/problem/14425)
---
## 문제 요약
총 N개의 문자열로 이루어진 집합 S가 주어진다.
입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

## 문제유형
해시

## 아이디어
1. 집합 S를 담아줄 set을 만들어준다(n만큼 loop돌기)
2. loop를 돌면서 m개의 문자열을 입력받는다.
3. 집합 s에 문자열이 포함되어있으면 카운트 +1 씩 해준다.

## 여담 

집합을 딕셔너리로 만들어서 써줘도 된다.

```python

import sys
input = sys.stdin.readline
n, m = map(int, input().split())

# s = set([input() for _ in range(n)]) 기존 set

s = {input()for _ in range(n)}
cnt = 0

for _ in range(m):
    check = input()
    if check in s:
        cnt += 1
print(cnt)

```
