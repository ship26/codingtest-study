import sys
input = sys.stdin.readline
n = int(input()) # 학생의 수
student = [] # 학생들의 몸무게 , 키를 받아줄 리스트
for _ in range(n):
    weight, height = map(int, input().split()) # 몸무게와 키를 받아준다.
    student.append([weight, height]) # 리스트에  넣는다.

for i in student: 
    rank = 1 # 1등에서 지면 +1씩 더해서 등수를 낮춰 줄것이라 초기값을 1로 설정.(한번도 안지면 1등)
    for j in student:
        if i[0] < j[0] and i[1] < j[1]: # i번째(0번째부터)애랑 처음부터 끝까지(j량) 다 비교하는게 i가 한번 도는거 i가 반복되면서 비교하는 코드 
                rank += 1 # 질때마다
    print(rank, end = " ") # 개행이 아닌 공백으로 이어주기.
