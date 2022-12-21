class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        i = 0 
        arr = []
        j = 0
        while i <len(nums):
            
            if nums[i] == 1:
                i= i+1
                j = j+1
            else:
                arr.append(j)
                i = i+1
                j = 0
        arr.append(j)
        return max(arr)
            
        """
        :type nums: List[int]
        :rtype: int
        """
        