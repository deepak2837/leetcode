#User function template for Python

class Solution:	
	def remove_duplicate(self, nums, N):
	    i = 0 
        j = 1
        while j<N:
            if nums[i] ==nums[j]:
                j = j+1
            else:
                if j ==i+1:
                    i = i +1
                    j = j+1
                else:
                    nums[i+1],nums[j] = nums[j],nums[i]
                    i = i+1
                    j = j+1
        return len(nums[:i+1])
		# code here


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends