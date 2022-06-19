import sys
input = sys.stdin.readline

def singletriangle(line):
    if line == 0:
        return '  *  '
    elif line == 1:
        return ' * * '
    else:
        return '*****'

def printdot(totalline, line):
    space = ' ' * (totalline // 2)
    if totalline == 3:
        print(singletriangle(line = line), end='')
    else:
        newtotalline = totalline // 2
        if line < newtotalline:
            print(space, end='')
            printdot(newtotalline, line = line % newtotalline)
            print(space, end='')
        else:
            printdot(newtotalline, line = line % newtotalline)
            print(end=' ')
            printdot(newtotalline, line = line % newtotalline)

N = int(input())
for i in range(N):
    printdot(N, i)
    print()