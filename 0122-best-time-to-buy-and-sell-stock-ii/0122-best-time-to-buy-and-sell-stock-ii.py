class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i  = 0 
        j = 1
       
        output_array = []
        while j <len(prices):
            
            lat_maxs = prices[j]-prices[i]
            i=i+1
            j = j+1
            output_array.append(lat_maxs)
        pro = 0
        for i in output_array:
            if i>0:
                pro = pro+i
        return pro