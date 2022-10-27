# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head 
        
        
        
        
        count = 0 
        while curr:
            count = count+1
            curr = curr.next
        # print(count)
        if k>count:
            return head
        
        n1 = None
        counts = 0
        currs = head
        while currs:
            counts = counts+1
            if counts==k:
                n1 = currs.val
                break
            else:
                currs = currs.next
        print(n1)
        n2 = None
        countss = 0
        currss = head
        while currss:
            countss = countss+1
            if countss==count-k+1:
                n2 = currss.val
                break
            else:
                currss = currss.next
        print(n2)
        
        if k==1:
            head.val =n2
        if count==2 and k ==2:
            temp = head.next.val
            head.next.val = head.val
            head.val= temp
            return head
        
        if k ==count:
            print("in this")
            head.val = n1
            f = head
            while f:
                if f.next==None:
                    f.val= n2
                f = f.next
            return head
            
        
        k1 = head
        for i in range(1,count+1):
            
        
            if i ==k-1:
                k1.next.val =n2
            if i ==count-k:
                k1.next.val = n1
            k1 = k1.next
                
        return head
        
            
        