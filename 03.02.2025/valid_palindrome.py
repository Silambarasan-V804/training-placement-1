class Solution(object):
    def isPalindrome(self, s):
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1  # Skip non-alphanumeric characters
            while left < right and not s[right].isalnum():
                right -= 1  # Skip non-alphanumeric characters
            
            if s[left].lower() != s[right].lower():
                return False  # Case insensitive comparison
            
            left += 1
            right -= 1
            
        return True
