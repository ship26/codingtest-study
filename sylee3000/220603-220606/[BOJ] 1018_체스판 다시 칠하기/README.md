# [BOJ] 1018_체스판 다시 칠하기

문제 링크 : https://www.acmicpc.net/problem/1018

------------------
## 문제 요약
  - N X M 의 판에서 8 X 8 의 체스판을 만들어내기 위해 새로 칠해야 할 정사각형 개수의 최소값을 구하는 문제

## 접근 방식
  - BWBWBWBW  
    WBWBWBWB  
    BWBWBWBW  
    WBWBWBWB  
    BWBWBWBW  
    WBWBWBWB  
    BWBWBWBW  
    WBWBWBWB << 직접 체스판 중 1가지 생성
  - 판 내에서 8 X 8 로 자를 수 있는 모든 경우의 수에 대해 체스판의 색과 다른 정사각형의 개수를 구함
  - 체스판의 색은 두가지 버전이 가능하고, 둘은 서로 완전 반대이기 때문에 min(체스1_칠해야 할 정사각형 수, 64 - 체스1_칠해야 할 정사각형 수)로 최소값을 구할 수 있다.
