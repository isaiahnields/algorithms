class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = list()
        self.helper(candidates, target, 0, res, [])
        return res
        
    def helper(self, candidates, target, idx, res, curr):
        if target == 0:
            res.append(tuple(curr))
        if target < 0:
            return
        for i in range(idx, len(candidates)):
            curr.append(candidates[i])
            self.helper(candidates, target - candidates[i], i, res, curr)
            curr.remove(candidates[i])
