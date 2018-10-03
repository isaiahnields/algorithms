class Solution:
    import re
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        maxx_word = None
        maxx_count = 0
        word_count = dict()
        for i in re.findall(r'[^\s\'!,.?":;0-9]+', paragraph):
            i = i.lower()
            if i not in banned:
                if i in word_count: word_count[i] += 1
                else: word_count[i] = 1
                if word_count[i] > maxx_count:
                    maxx_count = word_count[i]
                    maxx_word = i
        return maxx_word
