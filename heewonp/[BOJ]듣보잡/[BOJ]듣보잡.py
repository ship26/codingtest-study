import sys
input = sys.stdin.readline


n, m = map(int, input().split())

hear_set = set()
see_set = set()

for _ in range(n):
    hear_set.add(input())

for _ in range(m):
    see_set.add(input())

who_arr = sorted(list(hear_set & see_set))

print(len(who_arr))

for i in who_arr:
    print(i.strip())
