# [BOJ] 5430_AC

문제 링크 : https://www.acmicpc.net/problem/5430

------------------
## 문제 요약
  - AC의 함수 (R : 배열 뒤집기, D : 배열의 맨 앞 요소 제거, 없으면 error 출력)
  - 입력받은 함수를 수행한 결과를 출력하는 문제

## 접근 방식
  - deque 사용
  - R 함수가 실행될 때마다 is_reversed를 변경 (True, False 반복), 모든 함수가 실행이 끝났을 때 is_reversed가 True이면 배열을 뒤집는다.
  - D 함수가 실행될 때 count가 0이면 error 출력 후 break, 아니면 is_reversed에 따라 popleft나 pop을 실행하고 count를 1 감소시킨다.
