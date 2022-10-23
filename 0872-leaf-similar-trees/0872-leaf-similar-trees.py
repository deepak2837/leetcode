# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        list1 = []
        def printLeafNodes(root1):
            # If node is null, return
            if (not root1):
                return
            # If node is leaf node,
            # print its data
            if (not root1.left and not root1.right):
                list1.append(root1.val)
                return
            # If left child exists,
            # check for leaf recursively
            if root1.left:
                printLeafNodes(root1.left)
            # If right child exists,
            # check for leaf recursively
            if root1.right:
                printLeafNodes(root1.right)
        print(printLeafNodes(root1))
        
        
        
        
        list2 = []
        def printLeafNodes1(root2):
           
 
            # If node is null, return
            if (not root2):
                return

            # If node is leaf node,
            # print its data
            if (not root2.left and not root2.right):
                list2.append(root2.val)
                # print(root2.val,
                #       end = " ")
                return

            # If left child exists,
            # check for leaf recursively
            if root2.left:
                printLeafNodes1(root2.left)

            # If right child exists,
            # check for leaf recursively
            if root2.right:
                printLeafNodes1(root2.right)
        printLeafNodes1(root2)
        print(list2)
        if list1==list2:
            return True
        else:
            return False
        
        