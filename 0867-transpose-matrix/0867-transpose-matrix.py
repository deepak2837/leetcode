class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        number_col = len(matrix)
        number_row = len(matrix[0])
        master = []
        for i in range(number_row):
            minlist = []
            master.append(minlist)
            
            for j in range(number_col):
                print(i,j)
                print(matrix[j][i])
                minlist.append(matrix[j][i])
        return master
                
            
            
        
        