

n = input() #문자열로 받음
m = n
a = 0

while 1:
    if len(m) ==1  :# 1자리 수 라면
        m = '0' +m
    더하기 = str(int(m[0]) + int(m[1]))
    m = m[-1] + 더하기[-1]
    a +=1

    if m == n :
        print(a)
        break # 반복문 탈출