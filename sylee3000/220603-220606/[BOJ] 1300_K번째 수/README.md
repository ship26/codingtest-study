# [BOJ] 1300_K번째 수

문제 링크 : https://www.acmicpc.net/problem/1300

----------------------
## 문제 요약
  - N[i][j]=i * j 인 N * N 배열을 1차원 배열로 만든 배열을 B라고 한다.
  - B를 오름차순 정렬 했을 때, B[k]의 값을 구하는 문제

## 접근 방식
  - 이분 탐색, start=1, end=n^2
  - i번째 줄에서 mid 이하의 수의 개수 : min(mid // i, N)
  - 이를 모두 더한 값이 K보다 크면 K가 mid보다 작다는 뜻이므로 end=mid-1, 아니면 start=mid+1
