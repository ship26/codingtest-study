N = int(input())

pinary = [0, 1, 2]

if N >= 3:
    for i in range(3, N + 1):
        pinary.append((pinary[i-2] + pinary[i-1]) % 15746) 
print(pinary[N])
