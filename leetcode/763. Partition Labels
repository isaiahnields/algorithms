class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c: i for i, c in enumerate(S)}
        a = j = 0
        res = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                res.append(j - a + 1)
                a = j + 1
        return res
