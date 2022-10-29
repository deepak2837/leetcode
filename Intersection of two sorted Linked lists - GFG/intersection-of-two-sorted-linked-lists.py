#User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''

            
def findIntersection(a,b):
    dummy = Node(0)
    tail = dummy;
    dummy.next = None;
    def push(head_ref, new_data):
        new_node = Node(0)
        new_node.data = new_data;
        new_node.next = (head_ref);
        (head_ref) = new_node;   
        return head_ref
  
    ''' Once one or the other
    list runs out -- we're done '''
    while (a != None and b != None):
        if (a.data == b.data):
            tail.next = push((tail.next), a.data)
            tail = tail.next
            a = a.next
            b = b.next
         
        # advance the smaller list
        elif(a.data < b.data):
            a = a.next
        else:
            b = b.next
    
    return (dummy.next)
    

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # len1 = 0
        # len2 = 0
        # curr1 = head1
        # curr2 = head2
        # while curr1:
        #     len1+=1
        #     curr1= curr1.next
        # while curr2:
        #     len2+=1
        #     curr2= curr2.next
        # diff = max(len1,len2)-min(len1,len2)
  
        # if len2>len1:
        #     while diff:
        #         head2 = head2.next
        #         diff = diff-1
        # if len2<len1:
        #     while diff:
        #         head1 = head1.next
        #         diff = diff-1
        # while head1:
        #     if head1 == head2:
        #         return head1
        #     head1 = head1.next
        #     head2 = head2.next
        # return None

    #return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def insert(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

def printList(head):
    while head:
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        
        n1,n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)
        
        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)
        
        result = findIntersection(ll1.head,ll2.head)
        printList(result)
        print()

# } Driver Code Ends