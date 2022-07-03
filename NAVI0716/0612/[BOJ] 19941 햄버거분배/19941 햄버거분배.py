n, k=map(int,input().split())
n_l = list(input())
count=0
c1=0
for i in range(0,n):
    if n_l[i] == 'P':
        c1+=1
        for j in range(i-k,i+k+1):
            if c1 != count and j <= n-1 and n_l[j] == 'H' and j >= 0:
                n_l[j]='X'
                count+=1
                c1=count
print(count)