# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.prev = None
        
        def helper(head):
            if not head: return None
            helper(head.right)
            helper(head.left)
            head.left = None
            head.right = self.prev
            self.prev = head
        helper(root)
