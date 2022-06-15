nums = set(range(1,10001))
del_set = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    del_set.add(i)

nums = sorted(nums - del_set)

for k in nums:
    print(k)