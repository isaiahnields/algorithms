class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        seen = set()
        for email in emails:
            seen.add(email.split('@')[1] + '@' + email.split('+')[0].replace('.', ''))
        return len(seen)
