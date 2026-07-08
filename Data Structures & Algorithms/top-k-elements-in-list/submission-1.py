class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        min_heap=[]
        for num, freq in count.items():
            heapq.heappush(min_heap,(freq,num))   
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        final=[]
        for freq, num in min_heap:
            final.append(num)   
        return final                    



            
        