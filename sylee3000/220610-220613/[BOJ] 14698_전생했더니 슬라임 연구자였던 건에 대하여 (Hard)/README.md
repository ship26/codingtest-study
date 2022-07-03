# [BOJ] 14698_전생했더니 슬라임 연구자였던 건에 대하여 (Hard)

문제 링크 : https://www.acmicpc.net/problem/14698

-------------------
## 문제 요약
  - N 마리의 슬라임을 1마리로 합성한다.
  - 슬라임 에너지가 A, B인 두 마리의 슬라임을 합성하려면 A * B의 전기 에너지가 필요하다.
  - 합성 시에 발생하는 전기 에너지를 모두 곱한 값의 최소값을 구하는 문제

## 접근 방식
  - min heap 사용
  - 슬라임 에너지들을 한 줄로 입력받기 때문에 이를 리스트로 저장해주고, heapify() 함수를 사용해서 리스트를 min heap으로 만들어준다.
  ```
  slime_list = list(map(int, input().split()))
  heapq.heapify(slime_list)
  ```
  - min heap 내에서 가장 작은 값 두 개를 pop해서 총 에너지에 곱해주고, 곱한 값을 다시 min heap에 push해준다.
  - 이를 min heap 내에 하나의 값만 남을 때까지 반복해주면 답이 나오게 된다.
