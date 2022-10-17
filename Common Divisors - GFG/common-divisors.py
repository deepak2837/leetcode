#User function Template for python3
class Solution:
    def commDiv (self, a, b):
        k = min(a,b)
        count = 0 
        for i in range(1,k+1):
            if a%i==0 and b %i == 0:
                count = count+1
        return count 
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a, b = input().split()
        a = int(a)
        b = int(b)
        
        ob = Solution()
        print(ob.commDiv(a, b))
# } Driver Code Ends