import sys
input = sys.stdin.readline
n = int(input())

# 에라토스테네스 체
a = [False, False] + [True] * (n-1)
primes = []
for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False


start = 0
end = 0
answer = 0
sums = 0

while True:
    if sums >= n:
        sums -= primes[start]
        start += 1
    elif end == len(primes):
        break
    else:
        sums += primes[end]
        end += 1

    if sums == n:
        answer += 1