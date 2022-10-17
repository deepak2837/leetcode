class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        k = min(a,b)
        count = 0     
        for i in range(1,k+1):
            if a%i==0 and b%i==0:
                print(i)
                count= count+1
        return count
   
                
        