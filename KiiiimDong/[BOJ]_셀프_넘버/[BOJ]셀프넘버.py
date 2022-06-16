def n_self_number(n): # d(n)을 정의 
    number = n # 숫자가 들어오면
    for i in str(n): # 쪼개서 [3,3] 으로 나누고
        number += int(i) # 즉 33 + 3 + 3
    return number #그대로 리턴

n_self_list = [] #셀프넘버 아닌애들을 담을 배열

for i in range(10000): #10000까지 돌림
    n_self_list.append(n_self_number(i)) #셀프넘버 아닌 수을 넣어줌

for j in range(10000): #마찬가지로
    if j in n_self_list: # j에 arr랑 일치하는게 있으면 
        pass #그냥 pass
    else:
        print(j) #없으면 셀프넘버라는거니까 출력