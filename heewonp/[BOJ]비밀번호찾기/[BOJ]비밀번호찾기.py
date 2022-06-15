import sys
input = sys.stdin.readline

# 저장된 사이트 주소수, 찾으려는 사이트 주소수
n, m = map(int, input().split())

# 비밀번호와 사이트를 담아줄 hash를 선언
password_hash = {}

for _ in range(n):
    site, password = input().split()
    password_hash[site] = password # hash에 key:site, value:password 담아줌

for _ in range(m):
    # 찾으려는 사이트 주소
    search_site = input().strip()
    # 원하는 사이트의 비빌번호 출력
    print(password_hash[search_site])