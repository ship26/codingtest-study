
# N, M = map(int,input().split())
# list=[]
# N1=N
# out = 0
# list.append(N)
# count = 0
# while N > M :
#     N = N-M
#     count += 1
#
#     if count % M :
#         count += 1
# out=N1+count
# print(out)

# while True:
#     count+=1
#     list.append(list[0] // M)
#     if list[0]//M >0:

# for i in range(0,999):
#     if list[i] > M:
#         list.append(list[i] // M)
#     # if list[i+1] > M:
#     #     list.append(list[i+1]//M)
#     else:
#         break
# print(sum(list))

N, M = map(int,input().split())
# list=[]
# list.append(N)
#
# for i in range(0,999):
#     if list[i] > M:
#         list.append(list[i] // M)
#     else:
#         break
# print(list)
# print(sum(list))
t = N
while N:
    N = N//M
    t += N
print(t)