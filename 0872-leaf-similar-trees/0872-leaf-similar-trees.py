# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # //printinf the leaf nodes of first binary tree and appending their value in a list 
        list1 = []
        def printLeafNodes(root1):
            if (not root1):
                return
            if (not root1.left and not root1.right):
                list1.append(root1.val)
                return
            if root1.left:
                printLeafNodes(root1.left)
            if root1.right:
                printLeafNodes(root1.right)
        printLeafNodes(root1)

                
                
                
        # //printinf the leaf nodes of second binary tree and appending their value in a list
        list2 = []
        def printLeafNodes1(root2):
            if (not root2):
                return
            if (not root2.left and not root2.right):
                list2.append(root2.val)
                return
            if root2.left:
                printLeafNodes1(root2.left)
            if root2.right:
                printLeafNodes1(root2.right)
        printLeafNodes1(root2)
                
                
                
        # comapring the both list 
        if list1==list2:
            return True
        else:
            return False
        
        