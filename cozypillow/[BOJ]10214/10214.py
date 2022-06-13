case = int(input())
for i in range(case):
    Y = 0
    K = 0
    for i in range(9):
        y, k = map(int, input().split())
        Y += y
        K += k
    if Y == K:
        print("Draw")
    elif Y > K:
        print("Yonsei")
    elif K > Y:
        print("Korea")
