# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.total_tilt = 0
    
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.helper(root)
        return self.total_tilt
        
        
    def helper(self, root):
        if not root: return 0
        
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        self.total_tilt += abs(left_sum - right_sum)
        
        return root.val + left_sum + right_sum
