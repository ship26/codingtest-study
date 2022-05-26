h, m = map(int,(input().split()))
t = int(input())
plus_h = t // 60
plus_m = t % 60
h = h + plus_h
m = m + plus_m
if m >= 60:
    olim = m // 60
    m = m % 60
    h = h + olim
if h >= 24:
    h = h % 24
print(h, m)