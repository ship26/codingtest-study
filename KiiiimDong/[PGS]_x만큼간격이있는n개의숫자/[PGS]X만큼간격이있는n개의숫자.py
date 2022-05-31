def solution(x,n):
    answer_list = []
    for i in range(1,n+1):
        answer_list.append(x*i)
    return answer_list
print(solution(2,5))