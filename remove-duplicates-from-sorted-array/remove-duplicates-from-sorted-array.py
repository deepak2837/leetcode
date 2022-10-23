class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0 
        j = 1
        
        
        while j<len(nums):
            # print(nums)
            if nums[i] ==nums[j]:
                # print("in this if")
                j = j+1
            else:
                if j ==i+1:
                    i = i +1
                    j = j+1
                else:
                    nums[i+1],nums[j] = nums[j],nums[i]
                    i = i+1
                    j = j+1
        # print(i)
        return len(nums[:i+1])
                
      