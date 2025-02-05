class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        for c in columnTitle:
            result = result * 26 + ord(c) - ord('A') +1
        return result
