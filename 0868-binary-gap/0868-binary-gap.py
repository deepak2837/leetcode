class Solution:
    def binaryGap(self, n: int) -> int:
        
        number = bin(n).replace("0b","")
        number = list(number)
        print(number)
        
        maxs = 0
        i = 0 
        j = 1 
        while j<len(number):
            print(i,j)
            if number[i]=="1" and number[j]=="1":
                print(" in this 1")
                maxs = max(maxs,j-i)
                i = j
                j = j+1
                
            
            else:
                j = j+1
        return maxs
                
        