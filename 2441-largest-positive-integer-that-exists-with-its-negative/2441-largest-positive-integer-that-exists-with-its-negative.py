class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        min_element= min(nums)
        print(min_element)
        i = 0 
        k = len(nums)
        if len(nums)==0 or len(nums)==1:
            return -1
        while i<k:
            if -(min_element) in nums:
                return -(min_element)
            else:
                print(min_element)
                print(nums)
                nums.remove(min_element)
                print(nums)
                if len(nums)==1:
                    return -1
                else:
                    min_element = min(nums)
                i = i+1
                
        return -1
            
            
        
            
        