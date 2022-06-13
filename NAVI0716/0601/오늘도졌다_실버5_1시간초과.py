A = list(map(int,input().split()))
B = list(map(int,input().split()))
l=[]
for i in range(len(A)):
    if sum(A[0:i+1]) > sum(B[0:i+1]):
        l.append(1)

    else:
        l.append(0)
count= len(l)-1
if sum(A)<sum(B):    
    if A[0] != 0 or (sum(l[:count]) >= 1) or A[8] != 0: 
        print("Yes")    
    else:
        print("No")
        
        
================================================================

A = list(map(int,input().split()))
B = list(map(int,input().split()))
l=[]
A_I = 0
B_I = 0
ANS = 0
for i in range(len(A)):
    A_I = sum(A[0:i+1])
    if A_I > B_I:
        ANS = 1
    B_I = sum(B[0:i+1])
count= len(A)         
if ANS == 1 and (sum(A[:count]) < sum(B[:count])):
    print("Yes")
else:
    print("No")