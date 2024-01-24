import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        full_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
        res = ''
        for char in full_string[::-1]:
            res += char
        
        if res == full_string:
            return True
        else:
            return False
        
    # cara bang fikri
    # left, right = 0, len(s) - 1

    # while left < right:
    #     if not s[left].isalnum():
    #         left += 1
    #     elif not s[right].isalnum():
    #         right -= 1
    #     else:
    #         if s[left].lower() != s[right].lower():
    #             return False
    #         left += 1
    #         right -= 1
    # return True
        