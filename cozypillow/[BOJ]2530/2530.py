
# 입력
h, m, s = map(int, input().split()) # 현재 시, 분, 초
t = int(input()) # 초 단위

# 계산
plus_h = 0
plus_m = 0
plus_s = 0

if t >= 3600:
    plus_h += t // 3600
    t = t % 3600

if t >= 60:
    plus_m += t // 60
    t = t % 60

plus_s += t

s += plus_s
if s >= 60:
    s = s % 60
    plus_m += 1

m += plus_m
if m >= 60:
    m = m % 60
    plus_h += 1

h += plus_h
if h >= 24:
   while h >= 24:
       h = h % 24


# 출력
print(h,m,s)