def factorization(num):
    prime = 2
    while prime <= num:
        if num % prime == 0:
            print(prime)
            num = num // prime
        else:
            prime = prime + 1

num = int(input())
factorization(num)