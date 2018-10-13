# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        res = UndirectedGraphNode(node.label)
        seen = {node.label: res}
        self.helper(node, res, seen)
        return res
        
            
    def helper(self, node, answer, seen):
        seen[answer.label] = answer
        for i in node.neighbors:
            if i.label not in seen:
                nex = UndirectedGraphNode(i.label)
                answer.neighbors.append(nex)
                self.helper(i, nex, seen)
            else:
                answer.neighbors.append(seen[i.label])
