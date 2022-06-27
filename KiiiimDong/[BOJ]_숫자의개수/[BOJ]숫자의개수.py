import sys
input = sys.stdin.readline
num_list = []
for i in range(3):
    num_list.append(int(input()))
a = num_list[0]
b = num_list[1]
c = num_list[2]
product = a*b*c
for i in range(0,10):
    print(str(product).count(str(i)))