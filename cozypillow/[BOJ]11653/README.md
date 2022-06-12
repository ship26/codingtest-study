# 11653. 소인수분해

### [문제](https://www.acmicpc.net/problem/11653)
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.



### 입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

```
#입력 예시
72
```



### 출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.

```
#출력 예시
2
2
2
3
3
```



### 풀이

저는 내장함수나 다른 패키지들을 통해 소수들을 구할 줄 모릅니다.

 prime = 2로 시작해서, 

주어진 숫자가 prime으로 나누어 떨어지면 숫자를 prime으로 나누고

아니면 prime+=1 합니다.

4처럼 소수가 아닌 숫자로 나누어 질 것 같으면 진작에 2로 나눠지니까 괜찮습니다.

```python
def factorization(num):
    prime = 2
    while prime <= num:
        if num % prime == 0:
            print(prime)
            num = num // prime
        else:
            prime = prime + 1

num = int(input())
factorization(num)
```

