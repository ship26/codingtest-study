# [전화번호 목록](https://programmers.co.kr/learn/courses/30/lessons/42577)
---
## 1. 아이디어

### 해시를 이용한 방법
1. 전화번호 목록을 해시로 만들어 준다.
2. 접두어를 담아줄 변수를 선언한다
3. 전화번호 목록을 전체 번호 -> 전체 번호에서 번호 하나하나로 분리 시켜주고 변수에 담아준다.
4. 기존 번호와 같은 

### loop와 startswith를 사용한 방식
1. data를 정렬해준다.
2. 정렬을 하게되면 같은 접수두사가 있는경우 앞뒤로만 존재하게 됨.
즉, [119, 1195524421, 97674223] 순으로 정렬 
3. startswith를 이용해서 접두사가 있는지 확인


- startswith
startswith() : 문자열 시작부분에 존재하면 true, 존재하지 않으면 false
str.startswith(str)
