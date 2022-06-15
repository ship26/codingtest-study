def solution(phone_number):
    n = len(phone_number)
    real_number = phone_number[n-4:n] # n-4, n-3, n-2, n-1
    answer= '*'*(n-len(real_number)) + str(real_number)
    return answer