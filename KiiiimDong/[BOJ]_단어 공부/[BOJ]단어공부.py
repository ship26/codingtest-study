#import sys
#input = sys.stdin.readline 
n = input().upper() # zZa -> ZZA
word = list(set(n)) # ZZA -> ZA
word_count = []

for i in word: # 중복제거한 word에서
    word_count.append(n.count(i)) # i를 n(원래문장)에서의 개수를 세준다. (Z이 ZZA에 몇개들어가있는지, A가 ZZA에 몇개 들어가있는지) [2, 1]

max_number = max(word_count) # 맥스값(몇번셌는지의 맥스값) [2, 1] -> 2
if word_count.count(max_number) > 1:# 맥스값이 1개 보다 많으면
    print("?") 
else:
    max_index = word_count.index(max_number) # 맥스넘버를 갖는 인덱스를 추출. (0 인덱스) 
    print(word[max_index]) # word_count에 넣어준 인덱스대로 나오니깐 이렇게 가능. ZA에서 0인덱스 넣으면 Z

#print(word)
#print(word_count)
#print(max_index)
#print(word_count.count(max_number))