class Solution:
    def countTime(self, time: str) -> int:
        res = 1
        if time[0] =="?" and time[1]=="?":
            print("1")
            res = res*24
        
        if time[0] =="?" and time[1]!="?":
            print("2")
            if time[1]>="4":
                res = res*2
            else:
                res *= 3
            
        if time[0] !="?" and time[1]=="?":
            print("3")
            if time[0]<="1":
                res = res*10
            elif time[0]=="2":
                res *= 4
                
                
        if time[3] =="?" and time[4]=="?":
            print("4")
            res = res*60
        if time[3] =="?" and time[4]!="?":
            print("5")
            res = res*6
        if time[3] !="?" and time[4]=="?":
            print("6")
            res = res*10
        return res
       