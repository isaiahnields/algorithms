class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = dict()
        for p in prerequisites:
            if p[0] in d:
                d[p[0]].append(p[1])
            else:
                d[p[0]] = [p[1]]
        
        if len(d) == 0: return True
        
        while len(d) != 0:
            if not self.helper(d, list(d.keys())[0], set()):
                return False
            
        return True 
            
    def helper(self, d, k, visited):
        if k in visited:
            return False
        
        if k not in d:
            return True
        
        visited.add(k)
        
        no_cycle = True
        
        v = d[k]
        del d[k]
        for i in v:
            no_cycle &= self.helper(d, i, visited)
            
        return no_cycle 
