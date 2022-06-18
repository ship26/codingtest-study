N = input()
zero_count = 0
total_sum = 0
for i in N:
    if i == '0':
        zero_count += 1
    else:
        total_sum += int(i)

if total_sum % 3 == 0 and zero_count > 0:
    N = sorted(N, reverse=True)
    for i in range(len(N) - zero_count):
        print(N[i], end='')
    for i in range(zero_count):
        print(0, end='')
else:
    print(-1)
