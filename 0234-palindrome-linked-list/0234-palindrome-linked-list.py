
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #reverse function
#         def reverse(prev, head):
#             if not head:
#                 return prev
#             tmp = head.next
#             head.next = prev
#             return reverse(head, tmp)
        
    
        def reverse(head):
            previous = None
            curr = head 
            
            while curr:
                temp = curr.next
                curr.next = previous
                previous = curr
                curr = temp
            return previous
        #use slow and fast pointer to get the mid of list
        sp = head
        fp = sp
        while(fp and fp.next):
            sp = sp.next
            fp = fp.next.next
            
        mid = reverse(sp)
        
        #check for palindrome
        def check(mid, head):
            if(not mid):
                return True
            elif(mid.val == head.val):
                return check(mid.next, head.next)
            else:
                return False
            
        return check(mid, head)
