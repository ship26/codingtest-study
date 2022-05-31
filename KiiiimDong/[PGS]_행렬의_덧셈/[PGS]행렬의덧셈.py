answer = []
answer_list = []

arr1 = [[1,2],
        [2,3]]
arr2 = [[3,4],
        [5,6]]

for i in range(len(arr1)):
    for j in range(len(arr1[0])):
        answer_list.append(arr1[i][j] + arr2[i][j])
answer.append(answer_list[0:len(arr1[0])])
answer.append(answer_list[len(arr1[0]):])
print(answer)

# 예제는 통과하는데 제출에서 튕김(함수화 한것)
def solution(arr1, arr2):
    answer = []
    answer_list = []
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer_list.append(arr1[i][j] + arr2[i][j])
    answer.append(answer_list[0:len(arr1[0])])
    answer.append(answer_list[len(arr1[0]):])
    return answer

# 최종 제출
def solution(arr1, arr2) :
    answer = [[0] * len(arr1[0])] * (len(arr1))
    
    for i in range(len(arr1)) :
        answer[i] = [0] * len(arr1[0])
        for j in range(len(arr1[0])) :
            answer[i][j] = (arr1[i][j] + arr2[i][j]) 
    return answer