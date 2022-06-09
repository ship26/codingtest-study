case = int(input())
for i in range(case):
    result = 0
    mars = list(input().split())
    for j in range(len(mars)):
        if j == 0:
            result = float(mars[j])
        if mars[j] == '@':
            result = result * 3
        if mars[j] == '%':
            result = result + 5
        if mars[j] == '#':
            result = result - 7
    print(f'{result:.2f}')