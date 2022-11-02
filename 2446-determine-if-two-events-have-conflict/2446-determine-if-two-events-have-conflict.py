from datetime import datetime
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        if event2[1]<event1[0]:
            print("in this")
            event2,event1=event1,event2
        
        if event2[0]>event1[1]:
            return False
        else:
            return True