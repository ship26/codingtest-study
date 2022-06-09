# 9506. 약수들의 합



### [문제](https://www.acmicpc.net/problem/10214)
어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다. 

예를 들어 6은 6 = 1 + 2 + 3 으로 완전수이다.

n이 완전수인지 아닌지 판단해주는 프로그램을 작성하라.

### 입력
입력은 테스트 케이스마다 한 줄 간격으로 n이 주어진다. (2 < n < 100, 000)

입력의 마지막엔 -1이 주어진다.

```
#입력 예시
6
12
28
-1
```



### 출력
테스트케이스 마다 한줄에 하나씩 출력해야 한다.

n이 완전수라면, n을 n이 아닌 약수들의 합으로 나타내어 출력한다(예제 출력 참고).

이때, 약수들은 오름차순으로 나열해야 한다.

n이 완전수가 아니라면 n is NOT perfect. 를 출력한다.

```
#출력 예시
6 = 1 + 2 + 3
12 is NOT perfect.
28 = 1 + 2 + 4 + 7 + 14
```



### 풀이

while 반복문을 이용한 문제입니다.

number의 약수를 구해서 리스트에 넣었습니다.

출력할 때 리스트 속의 숫자들을 for문으로 자료형 변경해주기 귀찮아서 리스트를 두 개 만들어 각각 정수형과 문자열형으로 저장했습니다. 

```python
run = 1

while run == 1:
    number = int(input())
    if number == -1:
        run = 0

    else:
        yaksoos = []
        yaksoos_str = []
        yaksoo = 1
        while yaksoo < number:
            if number % yaksoo == 0:
                yaksoos.append(yaksoo)
                yaksoos_str.append(str(yaksoo))
            yaksoo += 1

        if sum(yaksoos) == number:
            result = " + ".join(yaksoos_str)
            print(f"{number} = {result}")
        else:
            print(f'{number} is NOT perfect.')