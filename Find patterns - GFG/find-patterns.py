#User function Template for python3
import math
class Solution:
    def numberOfSubsequences (self,S,W):

        # code here 

        ans = 0

        # initiallizing boolean arry to cjeck visited or not

        vis = [False]*len(S)

        for i in range(len(S)):

            

            if S[i] == W[0] and not vis[i]:

                #if it maches then it will mark as visited

                vis[i] = True

                #to move on the next sub string 

                j = i+1

                k = 1

                while j<len(S) and k<len(W):

                    if S[j] == W[k] and not vis[j]:

                        vis[j] = True

                        k +=1

                    j +=1

                

                if (k == len(W)):

                    ans +=1

                else:

                    break

        

        return ans
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends