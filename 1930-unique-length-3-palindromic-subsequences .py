from collections import Counter

def countPalindromicSubsequence(s: str) -> int:
    # jadi konsepnya ada left sebagai set dan right sebagai hashmap
    # yang kita iterate adalah mid
    # kalau huruf yang ada di left ada juga di right, maka kita bisa bikin palindrome
    
    res = set() # (mid_c, outer_c)
    left = set()
    right = Counter(s) # hashmap

    for m in s:
        right[m] -= 1
        for c in left:
            if right[c] > 0:
                res.add((m, c))
        left.add(m)

    return len(res)

# O(n^3) solution, will got TLE
# def countPalindromicSubsequence(self, s: str) -> int:
#         def is_palindrome(s):
#             return s == s[::-1]

#         res = set()

#         for i in range(len(s)-2):
#             for j in range(i+2, len(s)):
#                 if s[i] != s[j]:
#                     continue
#                 for k in range(i+1, j):
#                     word = [s[i], s[k], s[j]]
#                     combined = "".join(word)
#                     if is_palindrome(combined) and combined not in res:
#                         res.add(combined)
            
#         return len(res)