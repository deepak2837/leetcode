class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        j = []
        for i in range(1,n+1):
            if n%i==0:
                j.append(i)
                count = count+1
        print(j)
        if count==3:
            return True
        else:
            return False
                
        
        