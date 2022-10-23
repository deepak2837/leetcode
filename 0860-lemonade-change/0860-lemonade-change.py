class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0, 10:0, 20:0}
        for i in range(len(bills)) :
            print(d)
            if bills[i]==5:
                
                print("in 5")
                d[bills[i]] = d[bills[i]]+1
                print(d)
            if bills[i]==10:
                print("in 10")
                if d[5]>=1:
                    d[5]= d[5]-1
                    d[10]= d[10]+1
                else:
                    return False
            if bills[i]==20:
                print("in this 20")
                
                
                if d[5]>=1 and d[10]>=1:
                    print("in in this")
                    d[5]= d[5]-1
                    d[10]= d[10]-1
                    d[20] = d[20]+1
                elif d[5]>=3:
                    d[5]= d[5]-3
                    d[20]= d[20]+1
                else:
                    return False
               
        return True
                
                
        
        