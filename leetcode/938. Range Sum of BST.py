# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.result = 0
    
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.helper(root, L, R)
        return self.result
    
    def helper(self, root, L, R):
        if not root: return
        if L <= root.val <= R:
            self.result += root.val
        if L <= root.val: self.helper(root.left, L, R)
        if root.val <= R: self.helper(root.right, L, R)
