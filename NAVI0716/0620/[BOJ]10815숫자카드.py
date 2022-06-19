n = int(input())
a = set(input().split())
m = int(input())
b = list(input().split())
anwser = []
for i in b:
    if i not in a:
        print(0,end=" ")
    else:
        print(1,end=" ")