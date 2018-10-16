# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        level = [root]
        count = 0
        while level:
            new_level = []
            for node in level:
                if not node.left and not node.right: return count + 1
                if node.left: new_level.append(node.left)
                if node.right: new_level.append(node.right)
            level = new_level
            count += 1
