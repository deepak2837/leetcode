class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ax1= rec1[0]
        ay1=rec1[1]
        ax2 =rec1[2]
        ay2=rec1[3]
        bx1= rec2[0]
        by1=rec2[1]
        bx2 =rec2[2]
        by2=rec2[3]
        o =  max(min(ax2,bx2)- max(ax1,bx1),0) *  max(min(ay2,by2)-max(ay1,by1),0)
        
#         xx1=max(x1,x3)
#         xx2 =min(x2,x4)
#         yy1 = max(y1,y3)
#         yy2 = min(y2,y4)
#         xx3=xx2
#         yy3=yy1        
#         area=(xx1*(yy2-yy3) + xx2*(yy3-yy1) + xx3*(yy1-yy2))
        
        print(o)
        # print(xx1,yy1,xx2,yy2,xx3,yy3)
        if o>0:
            return True
        else:
            False