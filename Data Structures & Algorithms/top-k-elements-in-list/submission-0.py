class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket=[[] for i in range(len(nums)+1)]
        n_map={}
        result=[]
        for num in nums:
            n_map[num]=n_map.get(num,0)+1   
        for num,freq in n_map.items():
            bucket[freq].append(num)
        for i in range(len(bucket)-1,-1,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result)==k:
                    return result 
        return result                 



            
        