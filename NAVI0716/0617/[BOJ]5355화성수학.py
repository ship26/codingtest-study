n = int(input())
l=[]

for i in range(n):
    l_l = list(input().split())
    l.append(l_l)
for i in l:
    end = float(i[0])
    for j in range(1,len(i)):
        if i[j] == '@':
            end = end *3
        elif i[j] == '%':
            end =  end + 5
        else:
            end = end  -  7
    print(f"{end:.2f}")