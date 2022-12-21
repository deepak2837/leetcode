class Solution(object):
    def findNumbers(self, nums):
        cnt = 0 
        for i in range(len(nums)):
            if len(str(nums[i]))%2!=1:
                
                cnt = cnt+1
        return cnt
        """
        :type nums: List[int]
        :rtype: int
        """
        