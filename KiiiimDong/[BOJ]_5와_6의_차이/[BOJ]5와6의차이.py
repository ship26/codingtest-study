import sys
input = sys.stdin.readline
a, b = input().split()
max = int(a.replace('5','6')) + int(b.replace('5','6')) # replace가 문자열에 사용할 수 있는 함수라서  
min = int(a.replace('6','5')) + int(b.replace('6','5'))# 인풋을 문자열로 받고 replace 적용 후 값을 더할 때 int를 씀
print(min, max)