n = int(input())
l=[]
for i in range(n):
    count, anwser = input().split()
    end = ""
    count=int(count)
    for j in anwser:
        for k in range(count):
            end += j
    l.append(end)
for i in l:
    print(i)