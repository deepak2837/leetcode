class Solution(object):
    def duplicateZeros(self, nums):
        i= 0 
        while i<len(nums):
            
            if nums[i]==0:
                nums.pop()
                nums.insert(i+1,0)
                i= i+1
            i = i+1  
        print(nums)
                
                
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        