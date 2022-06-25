# [BOJ] 6603_로또

문제 링크 : https://www.acmicpc.net/problem/6603

----------------
## 문제 요약
  - 1~49 중 K개의 숫자를 입력받아 입력받은 숫자 중 6개를 고르는 방법을 출력하는 문제

## 접근 방식
  - 백트래킹
  - lotto_list의 길이가 6이 될 때까지 lotto_list에 없는 숫자들을 append
  - lotto_list의 길이가 6이 되면 lotto_list를 출력 후 return
