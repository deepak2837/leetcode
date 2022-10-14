# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        
        previous = None 
        curr = head 
        while curr:
            if curr.val== val:
                if curr == head:
                    head = head.next
                    curr = head
                else:
                    previous.next = curr.next
                   
                
                
                
                    curr = curr.next 
            else:
                previous = curr
                curr = curr.next
        return head
        