class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        listd  = []
        for i in lists:
            
            while i:
                listd.append(i.val)
                i = i.next
        print(listd)
        listd.sort()
        newnode=head = ListNode(0)
        print(listd)
        for i in listd:
        
            newnode.next =ListNode(i)
            newnode = newnode.next
        return head.next