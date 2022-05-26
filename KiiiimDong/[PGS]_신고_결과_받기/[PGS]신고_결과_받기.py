# id_list = ['muzi','frodo','apeach','neo']
# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2
# result =[2,1,1,0]

# 딕셔너리와 리스트만 사용한 풀이.
from collections import Counter
def solution(id_list, report ,k):
    report_dict = {} # 담아줄 딕셔너리
    check_list = [] # 중복을 제외한 신고리스트
    answer = [] # 정답 담을 리스트

    for report_id in id_list: # id_list에서 id를 꺼낸다.
        report_dict[report_id]= [] # 딕셔너리에 키값으로 id를 담는다.
    for case in report: 
        report_id, report_name = case.split() # 신고 문장에서 케이스를 꺼내서 분리한다. 
        # report_id = 신고한사람, report_name = 신고당한사람
        if report_name not in report_dict[report_id]: 
            report_dict[report_id].append(report_name) # 일단 딕셔너리에 신고한 사람을 키값으로 신고당한사람을 넣는다.

            check_list.append(report_name) # 체크리스트에 신고 당한사람을 기록한다.
    cnt_dict = Counter(check_list) # 신고 당한사람을 카운트한다.

    for report_id in id_list:
        answer.append(len([check for check in report_dict[report_id] if cnt_dict[check] >= k])) 
        # k회 이상 신고되어 정지 당한 사람을 신고한 모든 유저의 신고횟수 뽑아냄
    return answer

# set을 이용한 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list) # id_list만큼 0으로 초기화    
    reports = {x : 0 for x in id_list} 

    for r in set(report):
        reports[r.split()[1]] += 1 # set으로 중복되는것을 제거하고 난뒤에 신고당한사람 이름만 카운트.

    for r in set(report):
        if reports[r.split()[1]] >= k: # 신고횟수가 k번 이상이되면 작동
            answer[id_list.index(r.split()[0])] += 1 # 정지대상을 신고한 사람을 카운트.

    return answer    