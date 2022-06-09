from collections import Counter
import heapq
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        cnt_arr = Counter(arr)
        heap = []
        
        for key,value in cnt_arr.items():
             heapq.heappush(heap, (-value, key))
        
        # 최소힙이 기본인데 -를 붙여서 최대 힙으로 바꿔줌 [(-4, 3), (-3, 5), (-2, 2), (-1, 7)]
        # 최소힙일 경우 : [(1, 7), (2, 2), (3, 5), (4, 3)]


                
        cnt = 0
        size = len(arr)
        
        while heap and size > 0:
            value,key = heapq.heappop(heap)
            size -= -value
            # 배열의 길이에서 숫자의 개수 만큼 빼줌 (-를 붙여주는 이유는 기존 최대 힙을 만들 때 -를 사용해주었기때문에)
            cnt += 1
            
            if size <= len(arr)/2:
                return cnt