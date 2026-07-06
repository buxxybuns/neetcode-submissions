class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set={}
        for i in range(len(nums)):
            num=nums[i]
            comp=target-num
            if comp in num_set:
                return [num_set[comp],i]
            num_set[num]=i        


