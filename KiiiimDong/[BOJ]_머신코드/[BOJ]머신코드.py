import sys
import re

input = sys.stdin.readline
machine_code = input()
r = re.split('(?=[A-Z])', machine_code) # ?= 로 긍정탐색, [A-Z]는 알파벳 대문자
count = 0

for i in range(1, len(r)-1): # 맨뒤에 케이스는 빼야해서 len(r)-1까지
    a = len(r[i]) % 4 # 4로 나눈 나머지
    if a != 0: # 4로 안나눠지면
        count += (4-a) # (4-나머지) 만큼 nop이 입력되야하므로 이 갯수를 세면된다.
print(count)