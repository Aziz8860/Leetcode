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
        
    # neetcode's solution 1
    # newStr = ""
    # for c in s:
    #     if c.isalnum():
    #         newStr += c.lower()
    # return newStr == newStr[::-1]
        
    # cara bang fikri (paling oke)
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
        
    # neetcode's solution 2 (kalo gamau pake isalnum() jadi pake ascii)
    # l, r = 0, len(s) - 1

    # if you want to call another function inside of an object you have to use self keyword
    # while l < r:
    #     while l < r and not self.alphaNum(s[l]):
    #         l += 1
    #     while r < l and not self.alphaNum(s[r]):
    #         r -= 1
    #     if s[l].lower() != s[r].lower():
    #         return False
    #     l, r = l + 1, r - 1
    # return True
        
    # outside function
    # def alphaNum(self, c):
    #   return (ord('A') <= ord(c) <= ord('Z') or
    #           ord('a') <= ord(c) <= ord('z') or
    #           ord('0') <= ord(c) <= ord('9'))