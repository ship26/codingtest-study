# 해시를 이용한 풀이
def solution(participant, completion):
    temp = {}
    for part in participant:
        if part not in temp.keys():
            temp[part]= 0
        temp[part] += 1
    for com in completion:
        temp[com] -= 1
    for k in temp.keys():
        if temp[k] ==1:
            return k
            
            
            
# counter를 이용한 풀이
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    
    return list(answer.keys())[0] # list로 형 변환 후 0번째 인덱스 값을 읽어온다. 
    
    
'''

counter 생김새
{'A' :2 , 'B' : 3 ...}

return 부분 추가 설명
{'A':1} dict 값이 -> ['A']가 되고 [0]접근시, Stirng으로 가져오게 된다.

'''
