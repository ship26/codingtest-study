# [950. Reveal Cards In Increasing Order](https://leetcode.com/problems/reveal-cards-in-increasing-order/)
---
## 문제 요약
1. 주어진 덱 맨위의 카드를 가져와 공개하고 덱에서 카드를 꺼냄
2. 덱에 카드가 있으면 덱의 다음 맨 위 카드를 맨 아래에 놓음
3. 카드가 있으면 반복 없으면 중지
위의 순서가 숫자들이 순서대로 반복되어야 함

## 문제유형
큐

## 아이디어
1. 순서없이 주어진 덱을 정렬 해줌
2. 빈 덱을 하나 선언
3. 빈 덱에 맨 왼쪽에 정렬된 덱의 오른쪽 값을 넣어줌 
