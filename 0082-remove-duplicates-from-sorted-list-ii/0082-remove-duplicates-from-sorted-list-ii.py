# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        boom =  ListNode(0,head)
        piche = boom
        while head:
            if head.next and head.val ==head.next.val:
                while head.next and head.val ==head.next.val:
                    head = head.next
                piche.next = head.next
            else:
                piche = piche.next
                
                
            head= head.next
            
        return boom.next
            
            
            
        
        
        