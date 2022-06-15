# 10817. 세 수

~~어푸어푸 세수 아님 ㅎ~~

### [문제](https://www.acmicpc.net/problem/10817)
세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오. 



### 입력
첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

```
#입력 예시
20 30 10
```



### 출력
두 번째로 큰 정수를 출력한다.

```
#출력 예시
20
```



### 풀이

세 수를 받고,

리스트에 넣고,

정렬하고,

두 번째 수를 출력했습니다.

```python
A,B,C = map(int, input().split())

num_list = [A, B, C]
num_list = sorted(num_list)

print(num_list[1])