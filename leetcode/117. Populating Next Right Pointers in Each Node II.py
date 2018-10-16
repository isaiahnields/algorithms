# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return root
        level = [root]
        while level:
            for i in range(1, len(level)):
                if level[i - 1]: level[i - 1].next = level[i]
                    
            new_level = []
            for root in level:
                if root.left: new_level.append(root.left)
                if root.right: new_level.append(root.right)
            level = new_level
        
    def convert(self, node):
        if not node:
            return None
        else: return node.val
