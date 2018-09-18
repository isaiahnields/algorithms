# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [float('-inf')]
        self.traverse(root, res)
        return res[0]
    
    def traverse(self, root, res):
        if not root:
            return 0
        
        l = max(self.traverse(root.left, res), 0)
        r = max(self.traverse(root.right, res), 0)
        
        res[0] = max(root.val + l + r, res[0])
        
        return root.val + max(l, r)
