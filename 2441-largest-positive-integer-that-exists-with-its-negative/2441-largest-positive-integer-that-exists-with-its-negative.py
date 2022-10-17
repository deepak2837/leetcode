class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        for i in sorted(nums):
            print(sorted(nums))
            if i*-1 in nums:
                return abs(i)
        return -1
            
        