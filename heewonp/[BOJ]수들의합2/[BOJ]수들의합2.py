import sys
input = sys.stdin.readline
n,m = map(int,input().split())
num = list(map(int,input().split()))

start = 0
end = 0
cnt = 0
sums = 0


while True:
    if sums >= m:
        sums -= num[start]  # 부분합배열의합 >= 구해야하는 값 : start를 오른쪽으로 한칸이동하여 부분합배여크기 감소
        start += 1
    elif end == n: # end가 n 이되면 종료
        break
    else:
      sums += num[end] # 부분합배열의합 <= 구해야 하는 값 : end를 오른쪽으로 한칸 이동하여 부분합 배열의 크기를 증가
      end += 1

    if sums == m:
        cnt += 1
print(cnt)
